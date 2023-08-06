import argparse
from bf_nlu.cli.arguments import default_arguments
from bf_nlu.cli.arguments.run import add_server_arguments
from bf_nlu.constants import DEFAULT_bf_nlu_X_PORT
from bf_nlu.shared.constants import DEFAULT_DATA_PATH


def set_x_arguments(parser: argparse.ArgumentParser) -> None:
    default_arguments.add_model_param(parser, add_positional_arg=False)

    default_arguments.add_data_param(
        parser, default=DEFAULT_DATA_PATH, data_type="stories and bf_nlu NLU "
    )
    default_arguments.add_config_param(parser)
    default_arguments.add_domain_param(parser)

    parser.add_argument(
        "--no-prompt",
        action="store_true",
        help="Automatic yes or default options to prompts and oppressed warnings.",
    )

    parser.add_argument(
        "--production",
        action="store_true",
        help="Run bf_nlu X in a production environment.",
    )

    parser.add_argument(
        "--bf_nlu-x-port",
        default=DEFAULT_bf_nlu_X_PORT,
        type=int,
        help="Port to run the bf_nlu X server at.",
    )

    parser.add_argument(
        "--config-endpoint",
        type=str,
        help="bf_nlu X endpoint URL from which to pull the runtime config. This URL "
        "typically contains the bf_nlu X token for authentication. Example: "
        "https://example.com/api/config?token=my_bf_nlu_x_token",
    )

    add_server_arguments(parser)
