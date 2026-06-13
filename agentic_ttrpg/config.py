from datetime import datetime
from pathlib import Path

GAME_START = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
MODEL = "google-cloud:gemini-2.5-flash"
LOG_DIR = (Path(__file__).parent / f"../game_logs/{GAME_START}/").resolve()
LOG_DIR.mkdir(exist_ok=False, parents=True)
