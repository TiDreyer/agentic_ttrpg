import shutil
from datetime import datetime
from pathlib import Path

from agentic_ttrpg import config

_REPLACE_CHARS = set(" ,?!-:@$#()*&`'\"")


class NoteBook:
    """Class for a personal notebook for each Agent"""

    def __init__(self, player_name: str):
        self.player_name = self.__normalize_player_name(player_name)
        self.__note_dir = (config.LOG_DIR / "player_notes" / self.player_name).resolve()
        self.__deleted_dir = (config.LOG_DIR / "player_notes_deleted" / self.player_name).resolve()

    @staticmethod
    def __normalize_player_name(player_name: str) -> str:
        if not player_name.isalpha():
            raise ValueError("Player name needs to be a pure alphabetic string")
        return player_name

    @staticmethod
    def __normalize_note_name(note_name: str) -> str:
        for replace_char in _REPLACE_CHARS:
            note_name = note_name.replace(replace_char, "_")
        for name_part in note_name.split("/"):
            name_part_for_check = name_part.replace("_", "")
            if not name_part_for_check.isalnum():
                raise ValueError(f"Note name contains invalid characters:\n{note_name}")
        return note_name

    def __path(self, note_name: str) -> Path:
        """Turn a note name into a file path and ensure the parent folder exists"""
        note_name = self.__normalize_note_name(note_name)
        note_path = self.__note_dir / f"{note_name}.md"
        note_path.parent.mkdir(parents=True, exist_ok=True)
        return note_path.resolve()

    def write_note(self, note_name: str, note_text: str) -> None:
        note_path = self.__path(note_name=note_name)
        if note_path.is_file():
            self.delete_note(note_name=note_name)
        with open(note_path, "w") as note_file:
            note_file.write(note_text)

    def read_note(self, note_name: str) -> str | None:
        note_path = self.__path(note_name=note_name)
        if not note_path.is_file():
            return None
        with open(note_path, "r") as note_file:
            return note_file.read()

    def delete_note(self, note_name: str) -> None:
        note_path = self.__path(note_name=note_name)
        if not note_path.is_file():
            raise ValueError("Note does not exist")
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        deleted_path = self.__deleted_dir / f"{note_name}.{timestamp}.md"
        deleted_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(note_path, deleted_path)
    
    def list_notes(self) -> list[str]:
        note_names = []
        for file_name in self.__note_dir.iterdir():
            if file_name.is_file():
                note_names.append(file_name.name)
        return note_names
