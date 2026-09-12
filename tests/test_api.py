"""
Unit tests for Cricbuzz API client and offline fallback resilience.
"""
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api.cricbuzz_client import CricbuzzClient

def test_cricbuzz_client_fallback_matches():
    # Test client without API key to ensure fallback works flawlessly
    client = CricbuzzClient(api_key="")
    assert not client.is_api_configured()
    
    matches = client.get_live_matches()
    assert isinstance(matches, list)
    assert len(matches) > 0
    
    first = matches[0]
    assert "match_id" in first
    assert "team1" in first
    assert "team2" in first
    assert "status" in first

def test_cricbuzz_client_scorecard():
    client = CricbuzzClient(api_key="")
    scorecard = client.get_match_scorecard("1001")
    assert "batting_card" in scorecard
    assert "bowling_card" in scorecard
    assert len(scorecard["batting_card"]) > 0
    assert len(scorecard["bowling_card"]) > 0
