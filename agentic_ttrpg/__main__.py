from agentic_ttrpg import players

result = players.MARCUS.run_sync(
    "The game starts with a battle scene. Roll dice to see how many enemies are present and introduce the situation to the players"
)

print("\n" + 80 * "=")

for message in result.all_messages():
    print(repr(message))
    print(80 * "-")
