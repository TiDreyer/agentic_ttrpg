from pydantic_ai import Agent

from agentic_ttrpg import config, prompts, tools

__MAX_RETRIES = 3

MARCUS = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_MARCUS,
    tools=tools.GM_TOOLS,
    retries=__MAX_RETRIES,
)
CHLOE = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_CHLOE,
    tools=tools.PLAYER_TOOLS,
    retries=__MAX_RETRIES,
)
JULES = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_JULES,
    tools=tools.PLAYER_TOOLS,
    retries=__MAX_RETRIES,
)
MAYA = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_MAYA,
    tools=tools.PLAYER_TOOLS,
    retries=__MAX_RETRIES,
)
PRIYA = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_PRIYA,
    tools=tools.PLAYER_TOOLS,
    retries=__MAX_RETRIES,
)
SULLY = Agent(
    model=config.MODEL,
    system_prompt=prompts.SYSTEM_SULLY,
    tools=tools.PLAYER_TOOLS,
    retries=__MAX_RETRIES,
)
