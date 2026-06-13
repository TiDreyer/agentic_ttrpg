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


__CONVERSATION: list[SpokenWords] = []
__CONV_LOG_DIR = (config.LOG_DIR / "table_conversation").resolve()
__CONV_LOG_DIR.mkdir(exist_ok=False, parents=True)


def say(words: SpokenWords) -> None:
    with open(__CONV_LOG_DIR / str(uuid7()), "w") as word_log_file:
        word_log_file.write(repr(words))
    __CONVERSATION.append(words)
    print(words)
