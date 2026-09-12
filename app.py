"""
Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics
Main Application Entry Point.
"""
import streamlit as st
import config
from database.connection import initialize_database
from database.crud_operations import get_database_summary
from api.cricbuzz_client import CricbuzzClient

st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout=config.LAYOUT,
    initial_sidebar_state="expanded"
)

# Ensure database is initialized
initialize_database()

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4b5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        border-radius: 10px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    .metric-val {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }
    .metric-lbl {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        opacity: 0.9;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/color/96/cricket.png", width=70)
st.sidebar.title("🏏 Cricbuzz LiveStats")
st.sidebar.markdown("**Real-Time Cricket Insights & SQL Analytics**")
st.sidebar.divider()

# System Status in Sidebar
client = CricbuzzClient()
api_status = "🟢 Live API Active" if client.is_api_configured() else "🟠 Fallback Simulation Mode"
st.sidebar.markdown(f"**API Status:** {api_status}")
if not client.is_api_configured():
    st.sidebar.caption("Provide `RAPIDAPI_KEY` in `.env` to enable real-time RapidAPI Cricbuzz feeds.")

st.sidebar.divider()
st.sidebar.markdown("""
### 🧭 Navigation
- **1 🏠 Home**: System overview & Architecture
- **2 ⚡ Live Matches**: Real-time scorecards & commentary
- **3 📊 Top Player Stats**: Leaderboards & Head-to-Head
- **4 🔍 SQL Analytics**: 25 Business practice queries
- **5 🛠️ CRUD Operations**: Admin data management
""")

# Main Landing Page Content
st.markdown('<div class="main-header">🏏 Cricbuzz LiveStats Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">An End-to-End Cricket Analytics Platform integrating Real-Time REST APIs, a 3NF Relational SQL Database, and 25 Business Analytics Questions.</div>', unsafe_allow_html=True)

# Summary Metrics
summary = get_database_summary()
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.markdown(f'<div class="metric-card"><div class="metric-val">{summary.get("teams", 0)}</div><div class="metric-lbl">Teams</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="metric-card"><div class="metric-val">{summary.get("venues", 0)}</div><div class="metric-lbl">Venues</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="metric-card"><div class="metric-val">{summary.get("players", 0)}</div><div class="metric-lbl">Players</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="metric-card"><div class="metric-val">{summary.get("matches", 0)}</div><div class="metric-lbl">Matches</div></div>', unsafe_allow_html=True)
with c5:
    st.markdown(f'<div class="metric-card"><div class="metric-val">25</div><div class="metric-lbl">SQL Queries</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Feature Highlights Cards
col_left, col_right = st.columns(2)

with col_left:
    st.info("### ⚡ Real-Time Match Insights")
    st.markdown("""
    - Ingest live match updates, run rates, and fall of wickets from **Cricbuzz REST API**.
    - View over-by-over ball commentary with highlighted boundaries.
    - Automatic graceful fallback for uninterrupted demonstration without API quotas.
    """)
    if st.button("Explore Live Matches →", key="btn_live"):
        st.switch_page("pages/2_⚡_Live_Matches.py")

with col_right:
    st.success("### 🔍 25 SQL Analytical Queries")
    st.markdown("""
    - **Beginner (1-8)**: Aggregations, sorting, filters, role breakdowns.
    - **Intermediate (9-16)**: Multi-table JOINs, home/away wins, clutch performers.
    - **Advanced (17-25)**: CTEs, Window functions, composite ranking formulas, time-series momentum.
    """)
    if st.button("Explore SQL Analytics →", key="btn_sql"):
        st.switch_page("pages/4_🔍_SQL_Analytics.py")

st.divider()
st.markdown("""
#### 🛠️ Tech Stack:
`Python 3.10+` • `Streamlit` • `SQLite 3NF` • `Pandas` • `Plotly Express` • `Cricbuzz REST API` • `Requests`
""")
