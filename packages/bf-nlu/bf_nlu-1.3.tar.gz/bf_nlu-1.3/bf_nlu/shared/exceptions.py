import json
from typing import Optional, Text

import jsonschema
from ruamel.yaml.error import (
    MarkedYAMLError,
    MarkedYAMLWarning,
    MarkedYAMLFutureWarning,
)


class bf_nluException(Exception):
    """Base exception class for all errors raised by bf_nlu Open Source.

    These exceptions results from invalid use cases and will be reported
    to the users, but will be ignored in telemetry.
    """


class bf_nluCoreException(bf_nluException):
    """Basic exception for errors raised by bf_nlu Core."""


class bf_nluXTermsError(bf_nluException):
    """Error in case the user didn't accept the bf_nlu X terms."""


class InvalidParameterException(bf_nluException, ValueError):
    """Raised when an invalid parameter is used."""


class YamlException(bf_nluException):
    """Raised if there is an error reading yaml."""

    def __init__(self, filename: Optional[Text] = None) -> None:
        """Create exception.

        Args:
            filename: optional file the error occurred in"""
        self.filename = filename


class YamlSyntaxException(YamlException):
    """Raised when a YAML file can not be parsed properly due to a syntax error."""

    def __init__(
        self,
        filename: Optional[Text] = None,
        underlying_yaml_exception: Optional[Exception] = None,
    ) -> None:
        super(YamlSyntaxException, self).__init__(filename)

        self.underlying_yaml_exception = underlying_yaml_exception

    def __str__(self) -> Text:
        if self.filename:
            exception_text = f"Failed to read '{self.filename}'."
        else:
            exception_text = "Failed to read YAML."

        if self.underlying_yaml_exception:
            if isinstance(
                self.underlying_yaml_exception,
                (MarkedYAMLError, MarkedYAMLWarning, MarkedYAMLFutureWarning),
            ):
                self.underlying_yaml_exception.note = None
            if isinstance(
                self.underlying_yaml_exception,
                (MarkedYAMLWarning, MarkedYAMLFutureWarning),
            ):
                self.underlying_yaml_exception.warn = None
            exception_text += f" {self.underlying_yaml_exception}"

        if self.filename:
            exception_text = exception_text.replace(
                'in "<unicode string>"', f'in "{self.filename}"'
            )

        exception_text += (
            "\n\nYou can use https://yamlchecker.com/ to validate the "
            "YAML syntax of your file."
        )
        return exception_text


class FileNotFoundException(bf_nluException, FileNotFoundError):
    """Raised when a file, expected to exist, doesn't exist."""


class FileIOException(bf_nluException):
    """Raised if there is an error while doing file IO."""


class InvalidConfigException(ValueError, bf_nluException):
    """Raised if an invalid configuration is encountered."""


class UnsupportedFeatureException(bf_nluCoreException):
    """Raised if a requested feature is not supported."""


class SchemaValidationError(bf_nluException, jsonschema.ValidationError):
    """Raised if schema validation via `jsonschema` failed."""


class InvalidEntityFormatException(bf_nluException, json.JSONDecodeError):
    """Raised if the format of an entity is invalid."""

    @classmethod
    def create_from(
        cls, other: json.JSONDecodeError, msg: Text
    ) -> "InvalidEntityFormatException":
        """Creates `InvalidEntityFormatException` from `JSONDecodeError`."""
        return cls(msg, other.doc, other.pos)


class ConnectionException(bf_nluException):
    """Raised when a connection to a 3rd party service fails.

    It's used by our broker and tracker store classes, when
    they can't connect to services like postgres, dynamoDB, mongo.
    """
