from random import choice

from agentic_ttrpg import players, prompts, table_conversation

__MAX_TURNS = 20
__DEFAULT_TABLE_LOG_LENGTH = 20
__ACTIVE_PLAYERS = [
    players.CHLOE,
    players.JULES,
    players.MAYA,
    players.PRIYA,
    players.SULLY,
]
# give GM double chance of being called upon
__RANDOM_SET = __ACTIVE_PLAYERS + [players.MARCUS, players.MARCUS]


def __call_upon_player(player: players.Agent) -> None:
    prompt = (
        "These are the last things that happened at the table:\n"
        + table_conversation.transcript_record(__DEFAULT_TABLE_LOG_LENGTH)
        + prompts.INTERACTION_OPTION
    )
    players.react(player=player, prompt=prompt)


def main() -> None:
    # start and introduction round
    players.react(player=players.MARCUS, prompt=prompts.MODERATION_START)

    for player in __ACTIVE_PLAYERS:
        __call_upon_player(player=player)

    # main game loop - randomly switch between players
    for i in range(__MAX_TURNS):
        player = choice(__RANDOM_SET)
        __call_upon_player(player=player)

    # end of the game
    players.react(player=players.MARCUS, prompt=prompts.MODERATION_END)


main()
