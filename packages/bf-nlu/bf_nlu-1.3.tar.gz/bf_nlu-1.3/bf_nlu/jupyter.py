import asyncio
import pprint as pretty_print
import typing
from typing import Any, Dict, Optional, Text

from bf_nlu.shared.exceptions import bf_nluException
from bf_nlu.shared.utils.cli import print_success
import bf_nlu.core.agent
import bf_nlu.utils.common

if typing.TYPE_CHECKING:
    from bf_nlu.core.agent import Agent


def pprint(obj: Any) -> None:
    """Prints JSONs with indent."""
    pretty_print.pprint(obj, indent=2)


def chat(
    model_path: Optional[Text] = None,
    endpoints: Optional[Text] = None,
    agent: Optional["Agent"] = None,
) -> None:
    """Chat to the bot within a Jupyter notebook.

    Args:
        model_path: Path to a combined bf_nlu model.
        endpoints: Path to a yaml with the action server is custom actions are defined.
        agent: bf_nlu Core agent (used if no bf_nlu model given).
    """
    if model_path:
        agent = asyncio.run(
            bf_nlu.core.agent.load_agent(model_path=model_path, endpoints=endpoints)
        )

    if agent is None:
        raise bf_nluException(
            "Either the provided model path could not load the agent "
            "or no core agent was provided."
        )

    print("Your bot is ready to talk! Type your messages here or send '/stop'.")
    while True:
        message = input()
        if message == "/stop":
            break

        responses = asyncio.run(agent.handle_text(message))
        for response in responses:
            _display_bot_response(response)


def _display_bot_response(response: Dict) -> None:
    from IPython.display import Image, display

    for response_type, value in response.items():
        if response_type == "text":
            print_success(value)

        if response_type == "image":
            image = Image(url=value)
            display(image)
