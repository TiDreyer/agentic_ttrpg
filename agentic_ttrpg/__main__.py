from pydantic_ai import Agent

from agentic_ttrpg import config, prompts

game_master = Agent(model=config.MODEL, system_prompt=prompts.GM_SYSTEM)

result = game_master.run_sync("The game starts, introduce yourself to the players.")
print(result.output)
