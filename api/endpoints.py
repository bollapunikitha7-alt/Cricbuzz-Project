"""
Cricbuzz RapidAPI Endpoints and Headers configuration.
"""
import os
import config

RAPIDAPI_KEY = config.RAPIDAPI_KEY
RAPIDAPI_HOST = config.RAPIDAPI_HOST
BASE_URL = config.API_BASE_URL

HEADERS = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}

# RapidAPI Cricbuzz endpoints
LIVE_MATCHES_URL = f"{BASE_URL}/matches/v1/live"
RECENT_MATCHES_URL = f"{BASE_URL}/matches/v1/recent"
UPCOMING_MATCHES_URL = f"{BASE_URL}/matches/v1/upcoming"
MATCH_SCORECARD_URL = f"{BASE_URL}/mcenter/v1/{{match_id}}/scard"
MATCH_COMMENTARY_URL = f"{BASE_URL}/mcenter/v1/{{match_id}}/comm"
PLAYER_STATS_URL = f"{BASE_URL}/stats/v1/player/{{player_id}}"
SERIES_URL = f"{BASE_URL}/series/v1/international"
