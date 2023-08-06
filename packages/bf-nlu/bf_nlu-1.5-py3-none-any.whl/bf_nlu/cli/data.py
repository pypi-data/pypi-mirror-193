import argparse
import logging
from typing import List, TYPE_CHECKING

import bf_nlu.shared.core.domain
from bf_nlu import telemetry
from bf_nlu.cli import SubParsersAction
from bf_nlu.cli.arguments import data as arguments
from bf_nlu.cli.arguments import default_arguments
import bf_nlu.cli.utils
from bf_nlu.shared.constants import DEFAULT_DATA_PATH, DEFAULT_CONFIG_PATH
import bf_nlu.shared.data
from bf_nlu.shared.importers.bf_nlu import bf_nluFileImporter
import bf_nlu.shared.nlu.training_data.loading
import bf_nlu.shared.nlu.training_data.util
import bf_nlu.shared.utils.cli
import bf_nlu.utils.common
import bf_nlu.shared.utils.io

if TYPE_CHECKING:
    from bf_nlu.validator import Validator

logger = logging.getLogger(__name__)


def add_subparser(
    subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]
) -> None:
    """Add all data parsers.

    Args:
        subparsers: subparser we are going to attach to
        parents: Parent parsers, needed to ensure tree structure in argparse
    """
    data_parser = subparsers.add_parser(
        "data",
        conflict_handler="resolve",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Utils for the bf_nlu training files.",
    )
    data_parser.set_defaults(func=lambda _: data_parser.print_help(None))

    data_subparsers = data_parser.add_subparsers()

    _add_data_convert_parsers(data_subparsers, parents)
    _add_data_split_parsers(data_subparsers, parents)
    _add_data_validate_parsers(data_subparsers, parents)
    _add_data_migrate_parsers(data_subparsers, parents)


def _add_data_convert_parsers(
    data_subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]
) -> None:
    convert_parser = data_subparsers.add_parser(
        "convert",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Converts bf_nlu data between different formats.",
    )
    convert_parser.set_defaults(func=lambda _: convert_parser.print_help(None))

    convert_subparsers = convert_parser.add_subparsers()
    convert_nlu_parser = convert_subparsers.add_parser(
        "nlu",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Converts NLU data between formats.",
    )
    convert_nlu_parser.set_defaults(func=_convert_nlu_data)
    arguments.set_convert_arguments(convert_nlu_parser, data_type="bf_nlu NLU")


def _add_data_split_parsers(
    data_subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]
) -> None:
    split_parser = data_subparsers.add_parser(
        "split",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Splits bf_nlu data into training and test data.",
    )
    split_parser.set_defaults(func=lambda _: split_parser.print_help(None))

    split_subparsers = split_parser.add_subparsers()
    nlu_split_parser = split_subparsers.add_parser(
        "nlu",
        parents=parents,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        help="Performs a split of your NLU data into training and test data "
        "according to the specified percentages.",
    )
    nlu_split_parser.set_defaults(func=split_nlu_data)

    arguments.set_split_arguments(nlu_split_parser)


def _add_data_validate_parsers(
    data_subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]
) -> None:
    validate_parser = data_subparsers.add_parser(
        "validate",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Validates domain and data files to check for possible mistakes.",
    )
    _append_story_structure_arguments(validate_parser)
    validate_parser.set_defaults(func=validate_files)
    arguments.set_validator_arguments(validate_parser)

    validate_subparsers = validate_parser.add_subparsers()
    story_structure_parser = validate_subparsers.add_parser(
        "stories",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Checks for inconsistencies in the story files.",
    )
    _append_story_structure_arguments(story_structure_parser)
    story_structure_parser.set_defaults(func=validate_stories)
    arguments.set_validator_arguments(story_structure_parser)


def _append_story_structure_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--max-history",
        type=int,
        default=None,
        help="Number of turns taken into account for story structure validation.",
    )
    default_arguments.add_config_param(parser)


def split_nlu_data(args: argparse.Namespace) -> None:
    """Load data from a file path and split the NLU data into test and train examples.

    Args:
        args: Commandline arguments
    """
    data_path = bf_nlu.cli.utils.get_validated_path(args.nlu, "nlu", DEFAULT_DATA_PATH)
    data_path = bf_nlu.shared.data.get_nlu_directory(data_path)

    nlu_data = bf_nlu.shared.nlu.training_data.loading.load_data(data_path)
    extension = bf_nlu.shared.nlu.training_data.util.get_file_format_extension(data_path)

    train, test = nlu_data.train_test_split(args.training_fraction, args.random_seed)

    train.persist(args.out, filename=f"training_data{extension}")
    test.persist(args.out, filename=f"test_data{extension}")

    telemetry.track_data_split(args.training_fraction, "nlu")


def validate_files(args: argparse.Namespace, stories_only: bool = False) -> None:
    """Validates either the story structure or the entire project.

    Args:
        args: Commandline arguments
        stories_only: If `True`, only the story structure is validated.
    """
    from bf_nlu.validator import Validator

    config = bf_nlu.cli.utils.get_validated_path(
        args.config, "config", DEFAULT_CONFIG_PATH, none_is_valid=True
    )

    file_importer = bf_nluFileImporter(
        domain_path=args.domain, training_data_paths=args.data, config_file=config
    )

    validator = Validator.from_importer(file_importer)

    if stories_only:
        all_good = _validate_story_structure(validator, args)
    else:
        all_good = (
            _validate_domain(validator)
            and _validate_nlu(validator, args)
            and _validate_story_structure(validator, args)
        )

    telemetry.track_validate_files(all_good)
    if not all_good:
        bf_nlu.shared.utils.cli.print_error_and_exit(
            "Project validation completed with errors."
        )


def validate_stories(args: argparse.Namespace) -> None:
    """Validates that training data file content conforms to training data spec.

    Args:
        args: Commandline arguments
    """
    validate_files(args, stories_only=True)


def _validate_domain(validator: "Validator") -> bool:
    return (
        validator.verify_domain_validity()
        and validator.verify_actions_in_stories_rules()
        and validator.verify_forms_in_stories_rules()
        and validator.verify_form_slots()
        and validator.verify_slot_mappings()
    )


def _validate_nlu(validator: "Validator", args: argparse.Namespace) -> bool:
    return validator.verify_nlu(not args.fail_on_warnings)


def _validate_story_structure(validator: "Validator", args: argparse.Namespace) -> bool:
    # Check if a valid setting for `max_history` was given
    if isinstance(args.max_history, int) and args.max_history < 1:
        raise argparse.ArgumentTypeError(
            f"The value of `--max-history {args.max_history}` "
            f"is not a positive integer."
        )

    return validator.verify_story_structure(
        not args.fail_on_warnings, max_history=args.max_history
    )


def _convert_nlu_data(args: argparse.Namespace) -> None:
    import bf_nlu.nlu.convert

    if args.format in ["json", "yaml"]:
        bf_nlu.nlu.convert.convert_training_data(
            args.data, args.out, args.format, args.language
        )
        telemetry.track_data_convert(args.format, "nlu")
    else:
        bf_nlu.shared.utils.cli.print_error_and_exit(
            "Could not recognize output format. Supported output formats: 'json' "
            "and 'yaml'. Specify the desired output format with '--format'."
        )


def _add_data_migrate_parsers(
    data_subparsers: SubParsersAction, parents: List[argparse.ArgumentParser]
) -> None:
    migrate_parser = data_subparsers.add_parser(
        "migrate",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        parents=parents,
        help="Converts bf_nlu domain 2.0 format to required format for 3.0.",
    )
    migrate_parser.set_defaults(func=_migrate_domain)

    arguments.set_migrate_arguments(migrate_parser)


def _migrate_domain(args: argparse.Namespace) -> None:
    import bf_nlu.core.migrate

    bf_nlu.core.migrate.migrate_domain_format(args.domain, args.out)
