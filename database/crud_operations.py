"""
CRUD Operations Module for Cricbuzz LiveStats.
Provides modular, parameterized database operations for players, matches, teams, and venues.
"""
import pandas as pd
from typing import Optional, List, Dict, Any
from database.connection import execute_query, execute_non_query, get_connection

# ----------------- PLAYER OPERATIONS -----------------

def get_all_players(search_query: Optional[str] = None, 
                    team_id: Optional[int] = None, 
                    role: Optional[str] = None) -> pd.DataFrame:
    """Retrieve filtered player list with team details."""
    query = """
        SELECT 
            p.player_id, 
            p.full_name, 
            t.team_name, 
            p.playing_role, 
            p.batting_style, 
            p.bowling_style, 
            p.debut_year
        FROM players p
        JOIN teams t ON p.team_id = t.team_id
        WHERE 1=1
    """
    params = []
    if search_query:
        query += " AND p.full_name LIKE ?"
        params.append(f"%{search_query}%")
    if team_id:
        query += " AND p.team_id = ?"
        params.append(team_id)
    if role and role != "All":
        query += " AND p.playing_role = ?"
        params.append(role)
    
    query += " ORDER BY p.full_name ASC"
    return execute_query(query, tuple(params))

def get_player_by_id(player_id: int) -> Optional[Dict[str, Any]]:
    """Get single player details by player_id."""
    query = "SELECT * FROM players WHERE player_id = ?"
    df = execute_query(query, (player_id,))
    if not df.empty:
        return df.iloc[0].to_dict()
    return None

def create_player(full_name: str, team_id: int, playing_role: str, 
                  batting_style: str, bowling_style: str, debut_year: int) -> int:
    """Insert a new player record into the database."""
    query = """
        INSERT INTO players (full_name, team_id, playing_role, batting_style, bowling_style, debut_year)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    return execute_non_query(query, (full_name, team_id, playing_role, batting_style, bowling_style, debut_year))

def update_player(player_id: int, full_name: str, team_id: int, playing_role: str, 
                  batting_style: str, bowling_style: str, debut_year: int) -> int:
    """Update existing player record."""
    query = """
        UPDATE players
        SET full_name = ?, team_id = ?, playing_role = ?, batting_style = ?, bowling_style = ?, debut_year = ?
        WHERE player_id = ?
    """
    return execute_non_query(query, (full_name, team_id, playing_role, batting_style, bowling_style, debut_year, player_id))

def delete_player(player_id: int) -> int:
    """Delete player record and associated match stats."""
    query = "DELETE FROM players WHERE player_id = ?"
    return execute_non_query(query, (player_id,))

# ----------------- LOOKUP OPERATIONS -----------------

def get_teams() -> pd.DataFrame:
    """Retrieve all teams."""
    return execute_query("SELECT team_id, team_name, short_code, country FROM teams ORDER BY team_name ASC")

def get_venues() -> pd.DataFrame:
    """Retrieve all venues."""
    return execute_query("SELECT venue_id, venue_name, city, country, capacity FROM venues ORDER BY venue_name ASC")

def get_series() -> pd.DataFrame:
    """Retrieve all tournament series."""
    return execute_query("SELECT series_id, series_name, host_country, match_type FROM series ORDER BY start_date DESC")

# ----------------- MATCH OPERATIONS -----------------

def get_recent_matches_list(limit: int = 20) -> pd.DataFrame:
    """Retrieve recent matches with team names, venue, and victory details."""
    query = """
        SELECT 
            m.match_id,
            m.match_desc,
            m.match_format,
            m.match_date,
            t1.short_code AS team1,
            t2.short_code AS team2,
            v.venue_name,
            v.city,
            tw.team_name AS winner,
            m.win_margin,
            m.win_type,
            m.match_status
        FROM matches m
        JOIN teams t1 ON m.team1_id = t1.team_id
        JOIN teams t2 ON m.team2_id = t2.team_id
        JOIN venues v ON m.venue_id = v.venue_id
        LEFT JOIN teams tw ON m.match_winner_id = tw.team_id
        ORDER BY m.match_date DESC
        LIMIT ?
    """
    return execute_query(query, (limit,))

def create_match(series_id: int, match_desc: str, team1_id: int, team2_id: int,
                 venue_id: int, match_date: str, match_format: str,
                 toss_winner_id: int, toss_decision: str, match_winner_id: int,
                 win_margin: int, win_type: str, match_status: str = "Completed") -> int:
    """Insert a new match record."""
    query = """
        INSERT INTO matches (series_id, match_desc, team1_id, team2_id, venue_id,
                             match_date, match_format, toss_winner_id, toss_decision,
                             match_winner_id, win_margin, win_type, match_status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    return execute_non_query(query, (series_id, match_desc, team1_id, team2_id, venue_id,
                                     match_date, match_format, toss_winner_id, toss_decision,
                                     match_winner_id, win_margin, win_type, match_status))

# ----------------- DATABASE STATS -----------------

def get_database_summary() -> Dict[str, int]:
    """Return entity count summaries for dashboard display."""
    counts = {}
    tables = ['teams', 'venues', 'players', 'series', 'matches', 'player_match_batting', 'player_match_bowling']
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for t in tables:
            cursor.execute(f"SELECT COUNT(*) FROM {t}")
            counts[t] = cursor.fetchone()[0]
        return counts
    finally:
        conn.close()
