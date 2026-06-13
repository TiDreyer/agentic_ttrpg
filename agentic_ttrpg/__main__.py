from agentic_ttrpg import players, prompts, table_conversation

__MAX_ROUNDS = 5
__ACTIVE_PLAYERS = [
    players.CHLOE,
    players.JULES,
    players.MAYA,
    players.PRIYA,
    players.SULLY,
    players.MARCUS,
]


def main() -> None:
    players.MARCUS.run_sync(prompts.MODERATION_START)
    for i in range(__MAX_ROUNDS):
        print(f"[SYSTEM] Round {i}")
        for player in __ACTIVE_PLAYERS:
            print(f"[SYSTEM] active: {player}")
            prompt = (
                "These are the last things that happened at the table:\n"
                + table_conversation.transcript_record(len(__ACTIVE_PLAYERS))
                + prompts.INTERACTION_OPTION
            )
            player.run_sync(prompt)
    players.MARCUS.run_sync(prompts.MODERATION_END)


main()
