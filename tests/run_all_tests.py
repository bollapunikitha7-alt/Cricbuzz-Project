"""
Master Test Runner for Cricbuzz LiveStats.
"""
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.connection import initialize_database, execute_query
from database.crud_operations import (
    get_database_summary, get_all_players, create_player, get_player_by_id, update_player, delete_player
)
from sql.query_registry import QUERIES
from api.cricbuzz_client import CricbuzzClient

def run_tests():
    print("=== 1. TESTING DATABASE & CRUD ===")
    initialize_database()
    summary = get_database_summary()
    print("Database Summary:", summary)
    assert summary["teams"] >= 6
    assert summary["venues"] >= 10
    assert summary["players"] >= 30

    pid = create_player("Test Player", 1, "Batsman", "Right-hand bat", "None", 2024)
    p = get_player_by_id(pid)
    assert p["full_name"] == "Test Player"
    update_player(pid, "Test Player Updated", 1, "All-rounder", "Left-hand bat", "None", 2024)
    p_up = get_player_by_id(pid)
    assert p_up["full_name"] == "Test Player Updated"
    delete_player(pid)
    assert get_player_by_id(pid) is None
    print("Database & CRUD tests: PASS")

    print("\n=== 2. TESTING ALL 25 SQL QUERIES ===")
    failed = 0
    for q_id, q_data in sorted(QUERIES.items()):
        df = execute_query(q_data["sql"])
        rows, cols = df.shape
        if rows == 0:
            print(f"FAIL: Q{q_id:02d} returned 0 rows - {q_data['title']}")
            failed += 1
        else:
            cat = q_data["category"]
            title = q_data["title"]
            print(f"PASS: Q{q_id:02d} [{cat}] ({rows} rows, {cols} cols) - {title}")
            
    assert failed == 0, f"{failed} queries returned empty datasets!"
    print("\nAll 25 SQL Queries: 100% PASS!")

    print("\n=== 3. TESTING API CLIENT & FALLBACK ===")
    client = CricbuzzClient(api_key="")
    matches = client.get_live_matches()
    assert len(matches) > 0, "No live matches returned"
    scorecard = client.get_match_scorecard("1001")
    assert len(scorecard["batting_card"]) > 0, "Scorecard empty"
    print(f"API Client: PASS ({len(matches)} live matches parsed, scorecard verified)")

    print("\n============================================")
    print(" ALL TESTS PASSED SUCCESSFULLY! (100% GREEN)")
    print("============================================")

if __name__ == "__main__":
    run_tests()
