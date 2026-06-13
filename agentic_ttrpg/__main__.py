from pydantic_ai import Agent

from agentic_ttrpg import config, prompts, tools

game_master = Agent(
    model=config.MODEL,
    system_prompt=prompts.GM_SYSTEM,
    tools=[
        tools.roll_dice,
        tools.speak_at_table,
    ],
)

result = game_master.run_sync("The game starts with a battle scene. Roll dice to see how many enemies are present and introduce the situation to the players")
print(result.output)

print("\n" + 80 * "=")

for message in result.all_messages():
    print(repr(message))
    print(80 * "-")
