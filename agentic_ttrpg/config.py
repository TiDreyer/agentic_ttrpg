from datetime import datetime
from pathlib import Path

from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google_cloud import GoogleCloudProvider

GAME_START_DATE = datetime.now().strftime("%Y-%m-%d")
GAME_START_TIME = datetime.now().strftime("%H-%M-%S")

__GCP_PROVIDER = GoogleCloudProvider(location="global")
MODEL = GoogleModel("gemini-2.5-flash-lite", provider=__GCP_PROVIDER)

CONTEXT_DIR = (Path(__file__).parent / "../context/").resolve()
LOG_DIR = (Path(__file__).parent / f"../game_logs/{GAME_START_DATE}/{GAME_START_TIME}/").resolve()
LOG_DIR.mkdir(exist_ok=False, parents=True)
