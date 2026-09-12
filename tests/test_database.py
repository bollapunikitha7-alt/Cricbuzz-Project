"""
Unit tests for database schema, connection, and CRUD operations.
"""
import pytest
import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.connection import initialize_database, execute_query, get_connection
from database.crud_operations import (
    get_all_players, get_player_by_id, create_player, update_player, delete_player,
    get_teams, get_venues, get_database_summary
)

@pytest.fixture(scope="module", autouse=True)
def init_db():
    initialize_database()

def test_database_initialization():
    summary = get_database_summary()
    assert summary["teams"] >= 6
    assert summary["venues"] >= 10
    assert summary["players"] >= 30
    assert summary["matches"] >= 30

def test_crud_player_lifecycle():
    # 1. Create
    new_id = create_player(
        full_name="Test Cricketer",
        team_id=1,
        playing_role="Batsman",
        batting_style="Right-hand bat",
        bowling_style="None",
        debut_year=2024
    )
    assert new_id > 0

    # 2. Read
    player = get_player_by_id(new_id)
    assert player is not None
    assert player["full_name"] == "Test Cricketer"
    assert player["playing_role"] == "Batsman"

    # 3. Update
    rows = update_player(
        player_id=new_id,
        full_name="Test Cricketer Updated",
        team_id=1,
        playing_role="All-rounder",
        batting_style="Left-hand bat",
        bowling_style="Right-arm offbreak",
        debut_year=2024
    )
    updated_p = get_player_by_id(new_id)
    assert updated_p["full_name"] == "Test Cricketer Updated"
    assert updated_p["playing_role"] == "All-rounder"

    # 4. Delete
    delete_player(new_id)
    deleted_p = get_player_by_id(new_id)
    assert deleted_p is None
