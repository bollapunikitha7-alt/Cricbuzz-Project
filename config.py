"""
Configuration settings for Cricbuzz LiveStats application.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATABASE_DIR = BASE_DIR / "database"
DB_PATH = os.getenv("DB_PATH", str(BASE_DIR / "cricbuzz.db"))

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "cricbuzz-cricket.p.rapidapi.com")
API_BASE_URL = f"https://{RAPIDAPI_HOST}"

# Page configuration
APP_TITLE = "Cricbuzz LiveStats"
APP_ICON = "🏏"
LAYOUT = "wide"
