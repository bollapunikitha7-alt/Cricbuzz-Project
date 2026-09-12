"""
Top Player Stats Page: Multi-format leaderboards and head-to-head comparisons.
"""
import streamlit as st
import pandas as pd
from database.connection import execute_query
from utils.visualizer import plot_bar_chart, plot_grouped_bar_chart

st.set_page_config(page_title="Top Player Stats - Cricbuzz LiveStats", page_icon="📊", layout="wide")

st.title("📊 Top Player Statistics & Leaderboards")
st.markdown("Multi-format player evaluation, top scorers, leading wicket-takers, and interactive head-to-head comparisons.")

format_filter = st.selectbox("Filter Format:", ["All Formats", "Test", "ODI", "T20I"])
format_clause = f"WHERE m.match_format = '{format_filter}'" if format_filter != "All Formats" else ""

# Top Batting Leaderboard
tab_bat, tab_bowl, tab_compare = st.tabs(["🏏 Top Batsmen", "🎯 Top Bowlers", "⚖️ Player Comparison"])

with tab_bat:
    query_bat = f"""
        SELECT 
            p.full_name AS Player,
            t.short_code AS Team,
            SUM(b.runs_scored) AS Runs,
            ROUND(AVG(b.runs_scored), 2) AS Average,
            ROUND(AVG(b.strike_rate), 2) AS Strike_Rate,
            COUNT(CASE WHEN b.runs_scored >= 100 THEN 1 END) AS Centuries,
            COUNT(CASE WHEN b.runs_scored >= 50 AND b.runs_scored < 100 THEN 1 END) AS Fifties,
            MAX(b.runs_scored) AS High_Score
        FROM player_match_batting b
        JOIN players p ON b.player_id = p.player_id
        JOIN teams t ON p.team_id = t.team_id
        JOIN matches m ON b.match_id = m.match_id
        {format_clause}
        GROUP BY p.player_id, p.full_name, t.short_code
        ORDER BY Runs DESC
        LIMIT 10
    """
    bat_df = execute_query(query_bat)
    if not bat_df.empty:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.dataframe(bat_df, use_container_width=True, hide_index=True)
        with c2:
            fig = plot_bar_chart(bat_df.head(6), x="Player", y="Runs", title=f"Top Run Scorers ({format_filter})")
            st.plotly_chart(fig, use_container_width=True)

with tab_bowl:
    query_bowl = f"""
        SELECT 
            p.full_name AS Bowler,
            t.short_code AS Team,
            SUM(bw.wickets_taken) AS Wickets,
            ROUND(AVG(bw.economy_rate), 2) AS Economy,
            ROUND(AVG(bw.runs_conceded * 1.0 / NULLIF(bw.wickets_taken, 0)), 2) AS Average,
            SUM(bw.maidens) AS Maidens
        FROM player_match_bowling bw
        JOIN players p ON bw.player_id = p.player_id
        JOIN teams t ON p.team_id = t.team_id
        JOIN matches m ON bw.match_id = m.match_id
        {format_clause}
        GROUP BY p.player_id, p.full_name, t.short_code
        ORDER BY Wickets DESC, Economy ASC
        LIMIT 10
    """
    bowl_df = execute_query(query_bowl)
    if not bowl_df.empty:
        c1, c2 = st.columns([3, 2])
        with c1:
            st.dataframe(bowl_df, use_container_width=True, hide_index=True)
        with c2:
            fig = plot_bar_chart(bowl_df.head(6), x="Bowler", y="Wickets", title=f"Top Wicket Takers ({format_filter})")
            st.plotly_chart(fig, use_container_width=True)

with tab_compare:
    st.markdown("### 🥊 Head-to-Head Player Comparison")
    players_df = execute_query("SELECT player_id, full_name FROM players ORDER BY full_name ASC")
    player_names = players_df["full_name"].tolist()
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        p1 = st.selectbox("Select Player 1:", player_names, index=player_names.index("Virat Kohli") if "Virat Kohli" in player_names else 0)
    with col_p2:
        p2 = st.selectbox("Select Player 2:", player_names, index=player_names.index("Steve Smith") if "Steve Smith" in player_names else 1)
        
    compare_sql = """
        SELECT 
            p.full_name,
            COALESCE(SUM(b.runs_scored), 0) AS Total_Runs,
            ROUND(COALESCE(AVG(b.runs_scored), 0), 2) AS Batting_Avg,
            ROUND(COALESCE(AVG(b.strike_rate), 0), 2) AS Strike_Rate,
            COUNT(CASE WHEN b.runs_scored >= 100 THEN 1 END) AS Centuries,
            COALESCE(SUM(bw.wickets_taken), 0) AS Total_Wickets
        FROM players p
        LEFT JOIN player_match_batting b ON p.player_id = b.player_id
        LEFT JOIN player_match_bowling bw ON p.player_id = bw.player_id
        WHERE p.full_name IN (?, ?)
        GROUP BY p.player_id, p.full_name
    """
    res_df = execute_query(compare_sql, (p1, p2))
    if not res_df.empty:
        st.dataframe(res_df, use_container_width=True, hide_index=True)
        fig = plot_grouped_bar_chart(res_df, x="full_name", y1="Total_Runs", y2="Strike_Rate", 
                                     title="Comparison: Total Runs vs Strike Rate",
                                     label1="Total Runs", label2="Strike Rate")
        st.plotly_chart(fig, use_container_width=True)
