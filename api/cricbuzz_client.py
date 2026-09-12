"""
Cricbuzz API Ingestion Client with Resilience & Mock Fallback.
Handles live REST API communication, request timeouts, and graceful offline fallback.
"""
import requests
import logging
from typing import Dict, Any, List, Optional
import config
from api import endpoints

logger = logging.getLogger(__name__)

class CricbuzzClient:
    """Client for interacting with Cricbuzz REST API via RapidAPI."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or config.RAPIDAPI_KEY
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": config.RAPIDAPI_HOST
        }
        self.session = requests.Session()

    def is_api_configured(self) -> bool:
        """Check if a non-empty API key is present."""
        return bool(self.api_key and self.api_key.strip() and self.api_key != "your_rapidapi_key_here")

    def get_live_matches(self) -> List[Dict[str, Any]]:
        """Fetch live matches or return realistic fallback feed."""
        if self.is_api_configured():
            try:
                resp = self.session.get(endpoints.LIVE_MATCHES_URL, headers=self.headers, timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    matches = self._parse_api_matches(data)
                    if matches:
                        return matches
            except Exception as e:
                logger.warning(f"Failed to fetch live matches from API: {e}. Falling back to cached mock.")

        return self._get_fallback_live_matches()

    def get_match_scorecard(self, match_id: str) -> Dict[str, Any]:
        """Fetch match scorecard or return mock data."""
        if self.is_api_configured():
            url = endpoints.MATCH_SCORECARD_URL.format(match_id=match_id)
            try:
                resp = self.session.get(url, headers=self.headers, timeout=5)
                if resp.status_code == 200:
                    return resp.json()
            except Exception as e:
                logger.warning(f"Scorecard API call failed: {e}. Using fallback.")

        return self._get_fallback_scorecard(match_id)

    def _parse_api_matches(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse raw RapidAPI response format into normalized dictionary."""
        parsed = []
        try:
            type_matches = data.get("typeMatches", [])
            for tm in type_matches:
                series_matches = tm.get("seriesMatches", [])
                for sm in series_matches:
                    series_ad = sm.get("seriesAdWrapper", {})
                    for m in series_ad.get("matches", []):
                        m_info = m.get("matchInfo", {})
                        m_score = m.get("matchScore", {})
                        parsed.append({
                            "match_id": str(m_info.get("matchId", "")),
                            "match_desc": m_info.get("matchDesc", ""),
                            "series_name": m_info.get("seriesName", ""),
                            "team1": m_info.get("team1", {}).get("teamName", "Team 1"),
                            "team1_short": m_info.get("team1", {}).get("teamSName", "T1"),
                            "team2": m_info.get("team2", {}).get("teamName", "Team 2"),
                            "team2_short": m_info.get("team2", {}).get("teamSName", "T2"),
                            "status": m_info.get("status", "Live"),
                            "venue": m_info.get("venueInfo", {}).get("ground", "") + ", " + m_info.get("venueInfo", {}).get("city", ""),
                            "format": m_info.get("matchFormat", "ODI"),
                            "team1_score": self._format_score(m_score.get("team1Score", {})),
                            "team2_score": self._format_score(m_score.get("team2Score", {}))
                        })
        except Exception:
            pass
        return parsed

    def _format_score(self, score_obj: Dict[str, Any]) -> str:
        if not score_obj:
            return "Yet to bat"
        inngs1 = score_obj.get("inngs1", {})
        runs = inngs1.get("runs", 0)
        wkts = inngs1.get("wickets", 0)
        overs = inngs1.get("overs", 0)
        return f"{runs}/{wkts} ({overs} ov)"

    def _get_fallback_live_matches(self) -> List[Dict[str, Any]]:
        """High-fidelity mock live matches for robust offline experience."""
        return [
            {
                "match_id": "1001",
                "match_desc": "3rd T20I (N)",
                "series_name": "India vs Australia T20I Series 2026",
                "team1": "India",
                "team1_short": "IND",
                "team2": "Australia",
                "team2_short": "AUS",
                "status": "India need 24 runs in 18 balls to win",
                "venue": "Narendra Modi Stadium, Ahmedabad",
                "format": "T20I",
                "team1_score": "178/4 (17.0 ov)",
                "team2_score": "201/6 (20.0 ov)",
                "batting_team": "India",
                "target": 202,
                "current_rr": 10.47,
                "required_rr": 8.00
            },
            {
                "match_id": "1002",
                "match_desc": "2nd ODI (D/N)",
                "series_name": "England Tour of South Africa 2026",
                "team1": "South Africa",
                "team1_short": "SA",
                "team2": "England",
                "team2_short": "ENG",
                "status": "South Africa chose to bat",
                "venue": "Newlands, Cape Town",
                "format": "ODI",
                "team1_score": "285/5 (46.2 ov)",
                "team2_score": "Yet to bat",
                "batting_team": "South Africa",
                "target": None,
                "current_rr": 6.15,
                "required_rr": None
            },
            {
                "match_id": "1003",
                "match_desc": "1st Test - Day 3, Session 2",
                "series_name": "New Zealand Tour of Pakistan 2026",
                "team1": "Pakistan",
                "team1_short": "PAK",
                "team2": "New Zealand",
                "team2_short": "NZ",
                "status": "Pakistan lead by 142 runs",
                "venue": "Gaddafi Stadium, Lahore",
                "format": "Test",
                "team1_score": "340 & 165/3 (52.0 ov)",
                "team2_score": "363 (104.2 ov)",
                "batting_team": "Pakistan",
                "target": None,
                "current_rr": 3.17,
                "required_rr": None
            }
        ]

    def _get_fallback_scorecard(self, match_id: str) -> Dict[str, Any]:
        """Realistic scorecard detail for live match visualization."""
        if match_id == "1002":
            return {
                "match_id": "1002",
                "match_title": "South Africa vs England, 2nd ODI",
                "current_batsmen": [
                    {"name": "Heinrich Klaasen", "runs": 68, "balls": 44, "fours": 6, "sixes": 3, "sr": 154.55},
                    {"name": "David Miller", "runs": 41, "balls": 29, "fours": 3, "sixes": 2, "sr": 141.38}
                ],
                "current_bowler": {"name": "Mark Wood", "overs": 8.2, "maidens": 0, "runs": 56, "wickets": 2, "economy": 6.72},
                "batting_card": [
                    {"batsman": "Quinton de Kock (wk)", "dismissal": "c Buttler b Woakes", "runs": 74, "balls": 68, "fours": 8, "sixes": 2, "sr": 108.82},
                    {"batsman": "Temba Bavuma (c)", "dismissal": "b Rashid", "runs": 32, "balls": 48, "fours": 3, "sixes": 0, "sr": 66.67},
                    {"batsman": "Aiden Markram", "dismissal": "c Stokes b Wood", "runs": 45, "balls": 51, "fours": 4, "sixes": 1, "sr": 88.24},
                    {"batsman": "Heinrich Klaasen", "dismissal": "not out", "runs": 68, "balls": 44, "fours": 6, "sixes": 3, "sr": 154.55},
                    {"batsman": "David Miller", "dismissal": "not out", "runs": 41, "balls": 29, "fours": 3, "sixes": 2, "sr": 141.38}
                ],
                "bowling_card": [
                    {"bowler": "Chris Woakes", "overs": 9.0, "maidens": 1, "runs": 48, "wickets": 1, "economy": 5.33},
                    {"bowler": "Mark Wood", "overs": 8.2, "maidens": 0, "runs": 56, "wickets": 2, "economy": 6.72},
                    {"bowler": "Sam Curran", "overs": 8.0, "maidens": 0, "runs": 62, "wickets": 1, "economy": 7.75},
                    {"bowler": "Adil Rashid", "overs": 10.0, "maidens": 0, "runs": 52, "wickets": 1, "economy": 5.20},
                    {"bowler": "Ben Stokes", "overs": 6.0, "maidens": 0, "runs": 41, "wickets": 0, "economy": 6.83}
                ],
                "commentary": [
                    {"ball": "46.2", "comm": "Wood to Klaasen, FOUR! Slashed over backward point with ferocious power."},
                    {"ball": "46.1", "comm": "Wood to Miller, 1 run, driven firmly down to long-on."},
                    {"ball": "45.6", "comm": "Rashid to Klaasen, SIX! Tossed up on middle, Klaasen launches it straight over the sight screen!"},
                    {"ball": "45.5", "comm": "Rashid to Miller, 1 run, tucked into midwicket pocket."},
                    {"ball": "45.4", "comm": "Rashid to Klaasen, no run, beaten on the outside edge with a sharp leg-break."}
                ]
            }

        # Default match 1001 (IND vs AUS T20I thriller)
        return {
            "match_id": "1001",
            "match_title": "India vs Australia, 3rd T20I (Ahmedabad)",
            "current_batsmen": [
                {"name": "Suryakumar Yadav (c)", "runs": 64, "balls": 34, "fours": 6, "sixes": 4, "sr": 188.24},
                {"name": "Hardik Pandya", "runs": 28, "balls": 14, "fours": 2, "sixes": 2, "sr": 200.00}
            ],
            "current_bowler": {"name": "Mitchell Starc", "overs": 3.0, "maidens": 0, "runs": 36, "wickets": 1, "economy": 12.00},
            "batting_card": [
                {"batsman": "Rohit Sharma", "dismissal": "c Warner b Starc", "runs": 42, "balls": 21, "fours": 5, "sixes": 3, "sr": 200.00},
                {"batsman": "Shubman Gill", "dismissal": "b Hazlewood", "runs": 18, "balls": 15, "fours": 3, "sixes": 0, "sr": 120.00},
                {"batsman": "Virat Kohli", "dismissal": "c Carey b Zampa", "runs": 22, "balls": 18, "fours": 2, "sixes": 0, "sr": 122.22},
                {"batsman": "Suryakumar Yadav (c)", "dismissal": "not out", "runs": 64, "balls": 34, "fours": 6, "sixes": 4, "sr": 188.24},
                {"batsman": "Hardik Pandya", "dismissal": "not out", "runs": 28, "balls": 14, "fours": 2, "sixes": 2, "sr": 200.00}
            ],
            "bowling_card": [
                {"bowler": "Mitchell Starc", "overs": 3.0, "maidens": 0, "runs": 36, "wickets": 1, "economy": 12.00},
                {"bowler": "Josh Hazlewood", "overs": 4.0, "maidens": 0, "runs": 32, "wickets": 1, "economy": 8.00},
                {"bowler": "Pat Cummins", "overs": 4.0, "maidens": 0, "runs": 44, "wickets": 1, "economy": 11.00},
                {"bowler": "Adam Zampa", "overs": 4.0, "maidens": 0, "runs": 35, "wickets": 1, "economy": 8.75},
                {"bowler": "Glenn Maxwell", "overs": 2.0, "maidens": 0, "runs": 28, "wickets": 0, "economy": 14.00}
            ],
            "commentary": [
                {"ball": "17.0", "comm": "Starc to Pandya, SIX! Incredible strike! Full and in the slot, clattered over deep midwicket!"},
                {"ball": "16.5", "comm": "Starc to SKY, 1 run, yorker jammed out to deep third man."},
                {"ball": "16.4", "comm": "Starc to SKY, FOUR! Typical Surya flick over fine leg with supreme timing!"},
                {"ball": "16.3", "comm": "Starc to Pandya, 1 run, drilled hard straight to long-off."},
                {"ball": "16.2", "comm": "Starc to SKY, 2 runs, driven between cover and extra cover."}
            ]
        }
