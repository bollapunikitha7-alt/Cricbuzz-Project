"""
Home Page: System Architecture, Schema Details, and Data Dictionary.
"""
import streamlit as st
from database.crud_operations import get_database_summary
from database.connection import execute_query

st.set_page_config(page_title="Home - Cricbuzz LiveStats", page_icon="🏠", layout="wide")

st.title("🏠 Project Architecture & System Overview")
st.markdown("Detailed breakdown of the **Cricbuzz LiveStats** design, normalized data model, and technology stack.")

tab1, tab2, tab3 = st.tabs(["🏛️ Architecture Overview", "🗄️ Relational Schema (3NF)", "📈 Database Records Audit"])

with tab1:
    st.markdown("""
    ### Multi-Tiered Application Architecture
    The platform follows clean architectural principles separating the presentation, business logic, API ingestion, and persistence layers:
    """)
    
    st.code("""
    ┌─────────────────────────────────────────────────────────────┐
    │              STREAMLIT PRESENTATION LAYER                   │
    │  [Live Matches]  [Top Stats]  [SQL Analytics]  [CRUD Admin] │
    └──────────────┬──────────────────────────────┬───────────────┘
                   │                              │
                   ▼                              ▼
    ┌──────────────────────────────┐ ┌────────────────────────────┐
    │       API CLIENT LAYER       │ │   SQL ANALYTICS ENGINE     │
    │  - RapidAPI Cricbuzz Client  │ │  - 25 Pre-built Queries    │
    │  - Resilience & Offline Mock │ │  - Window Functions & CTEs │
    │  - JSON Schema Normalizer    │ │  - Query Performance Timer│
    └──────────────┬───────────────┘ └────────────┬───────────────┘
                   │                              │
                   ▼                              ▼
    ┌─────────────────────────────────────────────────────────────┐
    │           DATA PERSISTENCE & CRUD CONTROLLER                │
    │   - SQLite Thread-Safe Connection Pool                      │
    │   - 3NF Normalized Relational Schema (9 Tables)             │
    │   - Parameterized Transactions (Zero SQL Injection)         │
    └─────────────────────────────────────────────────────────────┘
    """, language="text")

with tab2:
    st.markdown("### Relational Data Model (Normalized 3NF)")
    st.markdown("""
    To satisfy all 25 complex SQL queries (including consecutive partnerships, format comparisons, and venue dynamics), the schema is structured into 9 normalized entities:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        1. **`teams`**: `team_id`, `team_name`, `short_code`, `country`
        2. **`venues`**: `venue_id`, `venue_name`, `city`, `country`, `capacity`
        3. **`players`**: `player_id`, `full_name`, `team_id`, `playing_role`, `batting_style`, `bowling_style`, `debut_year`
        4. **`series`**: `series_id`, `series_name`, `host_country`, `match_type`, `start_date`, `total_matches`
        5. **`matches`**: `match_id`, `series_id`, `match_desc`, `team1_id`, `team2_id`, `venue_id`, `match_date`, `match_format`, `toss_winner_id`, `toss_decision`, `match_winner_id`, `win_margin`, `win_type`, `match_status`
        """)
    with col2:
        st.markdown("""
        6. **`player_match_batting`**: `batting_id`, `match_id`, `player_id`, `innings`, `batting_position`, `runs_scored`, `balls_faced`, `fours`, `sixes`, `strike_rate`, `is_out`
        7. **`player_match_bowling`**: `bowling_id`, `match_id`, `player_id`, `innings`, `overs_bowled`, `maidens`, `runs_conceded`, `wickets_taken`, `economy_rate`
        8. **`player_match_fielding`**: `fielding_id`, `match_id`, `player_id`, `catches`, `stumpings`, `run_outs`
        9. **`batting_partnerships`**: `partnership_id`, `match_id`, `innings`, `batsman1_id`, `batsman2_id`, `partnership_runs`, `wicket_number`
        """)

with tab3:
    st.markdown("### Live Database Summary & Record Counts")
    summary = get_database_summary()
    st.json(summary)
    
    st.markdown("#### Sample Recent Matches in Database")
    recent_df = execute_query("SELECT match_id, match_desc, match_format, match_date, win_margin || ' ' || win_type AS margin FROM matches ORDER BY match_date DESC LIMIT 5")
    st.dataframe(recent_df, use_container_width=True)
