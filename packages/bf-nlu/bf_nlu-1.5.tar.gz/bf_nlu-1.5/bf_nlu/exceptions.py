from typing import Text
from packaging import version
from dataclasses import dataclass

from bf_nlu.shared.exceptions import bf_nluException
from bf_nlu.constants import MINIMUM_COMPATIBLE_VERSION


@dataclass
class UnsupportedModelVersionError(bf_nluException):
    """Raised when a model is too old to be loaded.

    Args:
        model_version: the used model version that is not supported and triggered
            this exception
    """

    model_version: Text

    def __str__(self) -> Text:
        minimum_version = version.parse(MINIMUM_COMPATIBLE_VERSION)
        return (
            f"The model version is trained using bf_nlu Open Source {self.model_version} "
            f"and is not compatible with your current installation "
            f"which supports models build with bf_nlu Open Source {minimum_version} "
            f"or higher. "
            f"This means that you either need to retrain your model "
            f"or revert back to the bf_nlu version that trained the model "
            f"to ensure that the versions match up again."
        )


class ModelNotFound(bf_nluException):
    """Raised when a model is not found in the path provided by the user."""


class NoEventsToMigrateError(bf_nluException):
    """Raised when no events to be migrated are found."""


class NoConversationsInTrackerStoreError(bf_nluException):
    """Raised when a tracker store does not contain any conversations."""


class NoEventsInTimeRangeError(bf_nluException):
    """Raised when a tracker store does not contain events within a given time range."""


class MissingDependencyException(bf_nluException):
    """Raised if a python package dependency is needed, but not installed."""


@dataclass
class PublishingError(bf_nluException):
    """Raised when publishing of an event fails.

    Attributes:
        timestamp -- Unix timestamp of the event during which publishing fails.
    """

    timestamp: float

    def __str__(self) -> Text:
        """Returns string representation of exception."""
        return str(self.timestamp)


class ActionLimitReached(bf_nluException):
    """Raised when predicted action limit is reached."""
