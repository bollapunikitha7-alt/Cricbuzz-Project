"""
Live Matches Page: Ingests Cricbuzz API feeds, renders scorecards, and commentary.
"""
import streamlit as st
import pandas as pd
from api.cricbuzz_client import CricbuzzClient
from utils.formatters import get_badge

st.set_page_config(page_title="Live Matches - Cricbuzz LiveStats", page_icon="⚡", layout="wide")

st.title("⚡ Live Match Center")
st.markdown("Real-time scorecards, fall of wickets, ball-by-ball commentary, and live run-rates.")

client = CricbuzzClient()

col_btn, col_stat = st.columns([1, 4])
with col_btn:
    refresh = st.button("🔄 Refresh Feed")
with col_stat:
    if client.is_api_configured():
        st.markdown(get_badge("Live RapidAPI Connected", "green"), unsafe_allow_html=True)
    else:
        st.markdown(get_badge("Simulated Live Feed (Offline Mode)", "amber"), unsafe_allow_html=True)

# Fetch Live Matches
matches = client.get_live_matches()

if not matches:
    st.warning("No ongoing matches found.")
    st.stop()

# Match Selection
match_options = {f"{m['team1_short']} vs {m['team2_short']} - {m['match_desc']} ({m['format']})": m['match_id'] for m in matches}
selected_title = st.selectbox("Select Match to Inspect:", list(match_options.keys()))
selected_id = match_options[selected_title]

# Selected Match Header Card
match_info = next(m for m in matches if m['match_id'] == selected_id)

st.markdown(f"""
<div style="background: white; border-left: 6px solid #2563eb; border-radius: 8px; padding: 18px; box-shadow: 0 2px 4px rgba(0,0,0,0.06); margin-top: 10px; margin-bottom: 20px;">
    <h3 style="margin: 0; color: #1e2937;">{match_info['team1']} vs {match_info['team2']}</h3>
    <p style="color: #6b7280; margin: 4px 0 12px 0;">{match_info['series_name']} • {match_info['venue']}</p>
    <div style="display: flex; gap: 30px; font-size: 1.2rem; font-weight: 600; color: #1f2937;">
        <div>{match_info['team1_short']}: <span style="color: #2563eb;">{match_info['team1_score']}</span></div>
        <div>{match_info['team2_short']}: <span style="color: #dc2626;">{match_info['team2_score']}</span></div>
    </div>
    <p style="margin-top: 10px; margin-bottom: 0; color: #059669; font-weight: 600;">Status: {match_info['status']}</p>
</div>
""", unsafe_allow_html=True)

# Load Scorecard details
scorecard = client.get_match_scorecard(selected_id)

col_score, col_comm = st.columns([3, 2])

with col_score:
    st.markdown("### 📋 Innings Scorecard")
    
    st.markdown("#### 🏏 Batting Card")
    batting_df = pd.DataFrame(scorecard.get("batting_card", []))
    if not batting_df.empty:
        st.dataframe(batting_df, use_container_width=True, hide_index=True)
    
    st.markdown("#### 🎯 Bowling Figures")
    bowling_df = pd.DataFrame(scorecard.get("bowling_card", []))
    if not bowling_df.empty:
        st.dataframe(bowling_df, use_container_width=True, hide_index=True)

with col_comm:
    st.markdown("### 🎙️ Ball-by-Ball Commentary")
    commentary = scorecard.get("commentary", [])
    for c in commentary:
        ball_style = "background: #2563eb; color: white;" if "SIX" in c['comm'] else ("background: #10b981; color: white;" if "FOUR" in c['comm'] else "background: #f3f4f6; color: #374151;")
        st.markdown(f"""
        <div style="margin-bottom: 10px; padding: 10px; border-radius: 6px; border: 1px solid #e5e7eb;">
            <span style="{ball_style} padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.85rem;">{c['ball']}</span>
            <span style="margin-left: 8px; font-size: 0.95rem;">{c['comm']}</span>
        </div>
        """, unsafe_allow_html=True)
