from pydantic_ai import Agent

from agentic_ttrpg import config, prompts, tools

MARCUS = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_MARCUS,
    tools=tools.GM_TOOLS,
)
CHLOE = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_CHLOE,
    tools=tools.PLAYER_TOOLS,
)
JULES = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_JULES,
    tools=tools.PLAYER_TOOLS,
)
MAYA = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_MAYA,
    tools=tools.PLAYER_TOOLS,
)
PRIYA = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_PRIYA,
    tools=tools.PLAYER_TOOLS,
)
SULLY = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_SULLY,
    tools=tools.PLAYER_TOOLS,
)
