from typing import Text

from bf_nlu.shared.exceptions import bf_nluCoreException


class AgentNotReady(bf_nluCoreException):
    """Raised if someone tries to use an agent that is not ready.

    An agent might be created, e.g. without an processor attached. But
    if someone tries to parse a message with that agent, this exception
    will be thrown.
    """

    def __init__(self, message: Text) -> None:
        """Initialize message attribute."""
        self.message = message
        super(AgentNotReady, self).__init__()


class ChannelConfigError(bf_nluCoreException):
    """Raised if a channel is not configured correctly."""


class InvalidTrackerFeaturizerUsageError(bf_nluCoreException):
    """Raised if a tracker featurizer is incorrectly used."""
