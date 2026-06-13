"""This module acts as a singleton that describes the conversation happening around the table"""

from uuid import uuid7

from pydantic import BaseModel

from agentic_ttrpg import config


class SpokenWords(BaseModel):
    words: str
    spoken_by: str
    spoken_as: str = "themself"
    way_of_speaking: str = "normal voice"

    def __str__(self) -> str:
        return f'{self.spoken_by} (as {self.spoken_as}, {self.way_of_speaking}): "{self.words}"'


class Action(BaseModel):
    description: str
    done_by: str

    def __str__(self) -> str:
        return f"[{self.done_by}] {self.description}"


__CONVERSATION: list[SpokenWords | Action] = []
__CONV_LOG_DIR = (config.LOG_DIR / "table_conversation").resolve()
__CONV_LOG_DIR.mkdir(exist_ok=False, parents=True)


def say(words: SpokenWords) -> None:
    """Say something at the table in a way that all players can hear"""
    with open(__CONV_LOG_DIR / str(uuid7()), "w") as word_log_file:
        word_log_file.write(str(words))
    __CONVERSATION.append(words)
    print(words)


def act(action: Action) -> None:
    """Perform a physical action at the table"""
    with open(__CONV_LOG_DIR / str(uuid7()), "w") as word_log_file:
        word_log_file.write(str(action))
    __CONVERSATION.append(action)
    print(action)


def read_transcript(max_interactions: int = 10, skip_last_n: int = 0) -> str:
    """Read the transcript of the last n interactions that happened at the table"""
    if skip_last_n > 0:
        last_n_things = __CONVERSATION[-max_interactions - skip_last_n : -skip_last_n]
    else:
        last_n_things = __CONVERSATION[-max_interactions:]
    print("[player reads transcript]")
    return "\n".join([str(thing) for thing in last_n_things])
