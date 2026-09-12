"""
CRUD Operations Page: Administrative management for Players, Matches, and Venues.
"""
import streamlit as st
import pandas as pd
from database.crud_operations import (
    get_all_players, get_player_by_id, create_player, update_player, delete_player,
    get_teams, get_venues, get_series, create_match, get_recent_matches_list
)

st.set_page_config(page_title="CRUD Operations - Cricbuzz LiveStats", page_icon="🛠️", layout="wide")

st.title("🛠️ Database CRUD Management")
st.markdown("Perform full Create, Read, Update, and Delete operations with form validation.")

tab_view, tab_add, tab_edit, tab_del, tab_match = st.tabs([
    "🔍 View Players", "➕ Add Player", "✏️ Edit Player", "🗑️ Delete Player", "🏏 Record Match"
])

teams_df = get_teams()
team_map = dict(zip(teams_df["team_name"], teams_df["team_id"]))
id_to_team = dict(zip(teams_df["team_id"], teams_df["team_name"]))

# 1. VIEW & SEARCH PLAYERS
with tab_view:
    st.markdown("### Search & Filter Players")
    c_search, c_team, c_role = st.columns(3)
    with c_search:
        search_kw = st.text_input("Search by Name:", placeholder="e.g. Virat")
    with c_team:
        selected_team_name = st.selectbox("Filter Team:", ["All"] + list(team_map.keys()))
        filter_team_id = team_map.get(selected_team_name) if selected_team_name != "All" else None
    with c_role:
        selected_role = st.selectbox("Filter Role:", ["All", "Batsman", "Bowler", "All-rounder", "Wicket-keeper"])

    players_df = get_all_players(search_query=search_kw, team_id=filter_team_id, role=selected_role)
    st.markdown(f"**Found {len(players_df)} players:**")
    st.dataframe(players_df, use_container_width=True, hide_index=True)

# 2. ADD NEW PLAYER
with tab_add:
    st.markdown("### Register New Player Record")
    with st.form("add_player_form", clear_on_submit=True):
        f_name = st.text_input("Full Name *", placeholder="e.g. Yashasvi Jaiswal")
        f_team = st.selectbox("Team *", list(team_map.keys()))
        f_role = st.selectbox("Playing Role *", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
        f_bat = st.selectbox("Batting Style *", ["Right-hand bat", "Left-hand bat"])
        f_bowl = st.selectbox("Bowling Style *", ["None", "Right-arm fast", "Right-arm medium", "Right-arm offbreak", "Right-arm legbreak", "Slow left-arm orthodox", "Left-arm wrist spin"])
        f_debut = st.number_input("Debut Year", min_value=1990, max_value=2026, value=2024, step=1)
        
        submitted = st.form_submit_button("✅ Create Player Record")
        if submitted:
            if not f_name.strip():
                st.error("Player name cannot be empty!")
            else:
                new_id = create_player(f_name.strip(), team_map[f_team], f_role, f_bat, f_bowl, int(f_debut))
                st.success(f"Player '{f_name}' successfully added with ID: {new_id}!")

# 3. EDIT PLAYER
with tab_edit:
    st.markdown("### Update Existing Player Details")
    all_p = get_all_players()
    if all_p.empty:
        st.info("No players available.")
    else:
        player_choices = {f"{row['full_name']} ({row['team_name']})": row['player_id'] for _, row in all_p.iterrows()}
        selected_p_label = st.selectbox("Select Player to Edit:", list(player_choices.keys()))
        selected_p_id = player_choices[selected_p_label]
        p_data = get_player_by_id(selected_p_id)
        
        if p_data:
            with st.form("edit_player_form"):
                u_name = st.text_input("Full Name", value=p_data["full_name"])
                current_team_idx = list(team_map.values()).index(p_data["team_id"]) if p_data["team_id"] in team_map.values() else 0
                u_team = st.selectbox("Team", list(team_map.keys()), index=current_team_idx)
                roles = ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"]
                u_role = st.selectbox("Playing Role", roles, index=roles.index(p_data["playing_role"]) if p_data["playing_role"] in roles else 0)
                bat_styles = ["Right-hand bat", "Left-hand bat"]
                u_bat = st.selectbox("Batting Style", bat_styles, index=bat_styles.index(p_data["batting_style"]) if p_data["batting_style"] in bat_styles else 0)
                u_bowl = st.text_input("Bowling Style", value=p_data["bowling_style"])
                u_debut = st.number_input("Debut Year", min_value=1990, max_value=2026, value=p_data["debut_year"] or 2020, step=1)
                
                u_submit = st.form_submit_button("💾 Save Changes")
                if u_submit:
                    update_player(selected_p_id, u_name.strip(), team_map[u_team], u_role, u_bat, u_bowl.strip(), int(u_debut))
                    st.success(f"Player '{u_name}' updated successfully!")

# 4. DELETE PLAYER
with tab_del:
    st.markdown("### Remove Player Record")
    st.warning("⚠️ Deleting a player will also cascade and remove their performance stats.")
    del_choices = {f"{row['full_name']} (ID: {row['player_id']})": row['player_id'] for _, row in all_p.iterrows()}
    del_label = st.selectbox("Select Player to Delete:", list(del_choices.keys()), key="del_select")
    del_id = del_choices[del_label]
    
    confirm = st.checkbox(f"I confirm I want to permanently delete player ID {del_id}")
    if st.button("🗑️ Delete Player", type="secondary", disabled=not confirm):
        delete_player(del_id)
        st.success(f"Player ID {del_id} successfully deleted from database.")

# 5. RECORD MATCH
with tab_match:
    st.markdown("### Record Completed Match Result")
    series_df = get_series()
    series_map = dict(zip(series_df["series_name"], series_df["series_id"]))
    venues_df = get_venues()
    venue_map = dict(zip(venues_df["venue_name"], venues_df["venue_id"]))
    
    with st.form("add_match_form"):
        m_series = st.selectbox("Series", list(series_map.keys()))
        m_desc = st.text_input("Match Description", placeholder="e.g. IND vs AUS, 1st T20I")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            m_t1 = st.selectbox("Team 1", list(team_map.keys()), index=0)
        with col_t2:
            m_t2 = st.selectbox("Team 2", list(team_map.keys()), index=1)
        m_venue = st.selectbox("Venue", list(venue_map.keys()))
        m_format = st.selectbox("Format", ["ODI", "T20I", "Test"])
        m_date = st.date_input("Match Date")
        
        col_toss, col_dec = st.columns(2)
        with col_toss:
            m_toss_win = st.selectbox("Toss Winner", [m_t1, m_t2])
        with col_dec:
            m_toss_dec = st.selectbox("Toss Decision", ["bat", "bowl"])
            
        col_win, col_margin, col_type = st.columns(3)
        with col_win:
            m_winner = st.selectbox("Match Winner", [m_t1, m_t2])
        with col_margin:
            m_margin = st.number_input("Victory Margin", min_value=1, max_value=500, value=25)
        with col_type:
            m_type = st.selectbox("Victory Type", ["runs", "wickets"])
            
        m_submit = st.form_submit_button("🏏 Save Match Record")
        if m_submit:
            match_new_id = create_match(
                series_map[m_series], m_desc, team_map[m_t1], team_map[m_t2],
                venue_map[m_venue], str(m_date), m_format,
                team_map[m_toss_win], m_toss_dec, team_map[m_winner],
                int(m_margin), m_type, "Completed"
            )
            st.success(f"Match successfully recorded with ID: {match_new_id}!")
