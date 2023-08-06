"""Global constants and definitions."""
from datetime import datetime
from pathlib import Path
from os import environ

MODULE_PATH = Path(__file__).resolve().parent

LOGGER_LEVEL = environ.get("LOGGER_LEVEL", "critical").upper()
LAUNCH_TIME = datetime.now().isoformat()
