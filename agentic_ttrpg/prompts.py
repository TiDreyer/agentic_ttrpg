from pathlib import Path
from textwrap import dedent

from agentic_ttrpg import config

_SESSION_GM = dedent("""
    You are acting as the game master in this session.
    """).strip()
_SESSION_PC = dedent("""
    You are acting as a player in this session.
    """).strip()

_PLAYER_TEMPLATE = dedent("""
    You are {player_name}, use this name whenever you refer to yourself.
    
    You are a professional improv artist playing a TTRPG in an actual play video format.
    Following is a short description of you:
    
    ---
    {player_profile}
    ---
    
    {session_prompt}
                          
    You can use this chat ONLY to plan your actions. Nothing you write here will be known to anybody else.
    Please use the appropriate tools for ALL communication at the table or interaction with the game.
    """).strip()


def __build_player_prompt(name: str, profile_path: Path, session_prompt: str) -> str:
    with open(profile_path, "r") as profile_file:
        profile = profile_file.read()
    prompt = _PLAYER_TEMPLATE.format(player_name=name, player_profile=profile, session_prompt=session_prompt)
    return prompt


SYSTEM_MARCUS = __build_player_prompt(name="Marcus", profile_path=config.CONTEXT_DIR / "player_marcus.md", session_prompt=_SESSION_GM)
SYSTEM_CHLOE = __build_player_prompt(name="Chloe", profile_path=config.CONTEXT_DIR / "player_chloe.md", session_prompt=_SESSION_PC)
SYSTEM_JULES = __build_player_prompt(name="Jules", profile_path=config.CONTEXT_DIR / "player_jules.md", session_prompt=_SESSION_PC)
SYSTEM_MAYA = __build_player_prompt(name="Maya", profile_path=config.CONTEXT_DIR / "player_maya.md", session_prompt=_SESSION_PC)
SYSTEM_PRIYA = __build_player_prompt(name="Priya", profile_path=config.CONTEXT_DIR / "player_priya.md", session_prompt=_SESSION_PC)
SYSTEM_SULLY = __build_player_prompt(name="Sully", profile_path=config.CONTEXT_DIR / "player_sully.md", session_prompt=_SESSION_PC)

MODERATION_START = "The game starts. Start moderating and ask every player to introduce themselves and their character."
MODERATION_END = "Your air time is over. Moderate the end of this episode."
INTERACTION_OPTION = "A camera pans to you. You have a chance to do something now."
