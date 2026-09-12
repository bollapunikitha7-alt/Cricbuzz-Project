"""
SQL Analytics Page: Interactive Runner for all 25 Practice Questions.
Features query metadata, execution timer, tabular output, visual charts, and CSV download.
"""
import streamlit as st
import time
from database.connection import execute_query
from sql.query_registry import QUERIES
from utils.visualizer import (
    plot_bar_chart, plot_grouped_bar_chart, plot_pie_chart, 
    plot_scatter_chart, plot_line_chart
)
from utils.formatters import get_badge

st.set_page_config(page_title="SQL Analytics - Cricbuzz LiveStats", page_icon="🔍", layout="wide")

st.title("🔍 SQL Analytics & Business Insights")
st.markdown("Explore and execute all **25 Industry-Grade SQL Queries** categorized by difficulty level.")

# Difficulty Filter
category_filter = st.radio(
    "Select Difficulty Tier:",
    ["All", "Beginner (1-8)", "Intermediate (9-16)", "Advanced (17-25)"],
    horizontal=True
)

filtered_queries = {}
for q_id, q in QUERIES.items():
    if category_filter == "All":
        filtered_queries[q_id] = q
    elif "Beginner" in category_filter and q["category"] == "Beginner":
        filtered_queries[q_id] = q
    elif "Intermediate" in category_filter and q["category"] == "Intermediate":
        filtered_queries[q_id] = q
    elif "Advanced" in category_filter and q["category"] == "Advanced":
        filtered_queries[q_id] = q

# Query Selection Dropdown
options = {f"Q{q_id:02d}: {q['title']} [{q['category']}]": q_id for q_id, q in filtered_queries.items()}
selected_label = st.selectbox("Select SQL Question:", list(options.keys()))
selected_id = options[selected_label]
query_data = QUERIES[selected_id]

# Badge Colors
badge_color = "green" if query_data["category"] == "Beginner" else ("amber" if query_data["category"] == "Intermediate" else "purple")

st.markdown(f"""
<div style="background: #ffffff; border: 1px solid #e5e7eb; border-radius: 8px; padding: 16px; margin: 12px 0 20px 0;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h3 style="margin: 0; color: #1e3a8a;">Question {selected_id}: {query_data['title']}</h3>
        {get_badge(query_data['category'], badge_color)}
    </div>
    <p style="color: #4b5563; margin-top: 8px; margin-bottom: 0;"><b>Business Context:</b> {query_data['business_problem']}</p>
</div>
""", unsafe_allow_html=True)

# SQL Query Viewer
with st.expander("📝 View SQL Query Syntax", expanded=True):
    st.code(query_data["sql"], language="sql")

# Execution Button & Metrics
col_exec, col_time, col_rows = st.columns([1, 1, 1])
with col_exec:
    run_btn = st.button("⚡ Execute Query", type="primary")

start_time = time.time()
df = execute_query(query_data["sql"])
exec_time_ms = round((time.time() - start_time) * 1000, 2)

with col_time:
    st.metric("Execution Time", f"{exec_time_ms} ms")
with col_rows:
    st.metric("Rows Returned", len(df))

# Results Section
st.markdown("### 📊 Query Results")
if df.empty:
    st.info("Query executed successfully but returned 0 rows.")
else:
    c_tab, c_chart = st.tabs(["📋 Result Table", "📈 Visualization"])
    
    with c_tab:
        st.dataframe(df, use_container_width=True, hide_index=True)
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV",
            data=csv_data,
            file_name=f"cricbuzz_q{selected_id}_results.csv",
            mime="text/csv"
        )
        
    with c_chart:
        chart_type = query_data.get("chart_type", "table")
        if chart_type == "bar" and "x" in query_data and "y" in query_data:
            fig = plot_bar_chart(df, x=query_data["x"], y=query_data["y"], title=query_data["title"])
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "pie" and "chart_col" in query_data and "chart_val" in query_data:
            fig = plot_pie_chart(df, names=query_data["chart_col"], values=query_data["chart_val"], title=query_data["title"])
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "grouped_bar" and "x" in query_data:
            fig = plot_grouped_bar_chart(df, x=query_data["x"], y1=query_data["y1"], y2=query_data["y2"], title=query_data["title"])
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "scatter" and "x" in query_data and "y" in query_data:
            fig = plot_scatter_chart(df, x=query_data["x"], y=query_data["y"], title=query_data["title"])
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "line" and "x" in query_data and "y" in query_data:
            fig = plot_line_chart(df, x=query_data["x"], y=query_data["y"], title=query_data["title"])
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("A specialized tabular format is most appropriate for this multidimensional query.")
            st.dataframe(df, use_container_width=True)
