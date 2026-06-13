from random import randint
from typing import Literal

from pydantic_ai import Tool

from agentic_ttrpg import table_conversation


def _roll_dice(type_of_dice: Literal[2, 4, 6, 8, 10, 12, 20, 100] = 20, number_of_dice: int = 1) -> str:
    """Roll n dice of a given type and return the individual results as well as the sum"""
    if number_of_dice < 1:
        return "You can only roll a number of dice greater than zero"
    results = [randint(1, type_of_dice) for _ in range(number_of_dice)]
    return_str = f"sum({results}) = {sum(results)}"
    return return_str


PLAYER_TOOLS = [
    Tool(_roll_dice, takes_ctx=False),
    Tool(table_conversation.say, takes_ctx=False),
    Tool(table_conversation.act, takes_ctx=False),
    Tool(table_conversation.read_transcript, takes_ctx=False),
]
GM_TOOLS = PLAYER_TOOLS + []
