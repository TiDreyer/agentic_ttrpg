import json
from uuid import uuid7

from pydantic_ai import Agent

from agentic_ttrpg import config, prompts, tools

__MAX_RETRIES = 3
__AGENT_LOG_DIR = (config.LOG_DIR / "agent_runs").resolve()
__AGENT_LOG_DIR.mkdir(exist_ok=False, parents=True)

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


def react(player: Agent, prompt: str) -> None:
    response = player.run_sync(prompt)
    messages = json.loads(response.all_messages_json().decode())
    with open(__AGENT_LOG_DIR / f"{uuid7()}.json", "w") as word_log_file:
        json.dump(fp=word_log_file, obj=messages, indent=2)
