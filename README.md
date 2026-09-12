# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B.svg)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/Database-SQLite%203NF-003B57.svg)](https://www.sqlite.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Express-3F4F75.svg)](https://plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end, production-grade sports analytics platform integrating real-time Cricbuzz REST API data, a normalized 3NF relational SQL database, an analytical engine solving **25 industry business practice queries**, full administrative CRUD operations, and an interactive multi-page Streamlit web dashboard.

---

## 📌 Features & Page Architecture

1. **🏠 Home & Architecture (`pages/1_🏠_Home.py`)**
   - Multi-tier system architecture documentation.
   - 3NF relational data dictionary with foreign key relationships.
   - Real-time database table health and audit counters.
2. **⚡ Live Match Center (`pages/2_⚡_Live_Matches.py`)**
   - Real-time match status from Cricbuzz REST API.
   - Comprehensive scorecards: batsmen runs, balls, 4s, 6s, strike rates, bowler overs, maidens, wickets, economy rates.
   - Ball-by-ball commentary feed with boundary highlights.
   - Resilient offline fallback simulation for testing without API quotas.
3. **📊 Top Player Stats (`pages/3_📊_Top_Player_Stats.py`)**
   - Format filtering: Test, ODI, T20I, All Formats.
   - Top Batsmen & Top Bowlers leaderboards.
   - Interactive Head-to-Head player comparison engine.
4. **🔍 SQL Analytics Engine (`pages/4_🔍_SQL_Analytics.py`)**
   - Categorized by difficulty: **Beginner (1-8)**, **Intermediate (9-16)**, **Advanced (17-25)**.
   - One-click query execution with performance latency metrics (ms).
   - Dynamic interactive Plotly charts tailored to query logic.
   - CSV export for query results.
5. **🛠️ CRUD Operations (`pages/5_🛠️_CRUD_Operations.py`)**
   - Form-based administration for Players and Matches.
   - Create, Search/Filter, Update, and Delete with foreign key cascade safety.

---

## 🧮 25 SQL Analytical Business Queries

| # | Question Title | Difficulty | SQL Concepts Applied |
|---|---|---|---|
| **Q1** | Indian Players Profile | Beginner | `SELECT`, `JOIN`, `WHERE`, `ORDER BY` |
| **Q2** | Matches in Last 30 Days | Beginner | `julianday()`, Date arithmetic, `JOIN` |
| **Q3** | Top 10 ODI Run Scorers | Beginner | `SUM()`, `AVG()`, `COUNT(CASE)`, `GROUP BY` |
| **Q4** | Venues Capacity > 50,000 | Beginner | Numeric filtering, `ORDER BY DESC` |
| **Q5** | Match Win Count per Team | Beginner | `COUNT()`, `GROUP BY`, `ORDER BY` |
| **Q6** | Player Count per Playing Role | Beginner | Distribution aggregation, `GROUP BY` |
| **Q7** | Format-wise Peak Batting Scores | Beginner | `MAX()`, multi-group aggregation |
| **Q8** | Series Starting in 2024 | Beginner | `strftime('%Y')` date extraction |
| **Q9** | All-Rounder Multi-Format Stats | Intermediate | Multi-table `JOIN`, `HAVING` filters |
| **Q10** | Last 20 Matches & Margins | Intermediate | Multi-table joins, victory margins |
| **Q11** | Cross-Format Performance Comparison | Intermediate | Conditional aggregation, `HAVING COUNT(DISTINCT)` |
| **Q12** | Home vs Away Win Analysis | Intermediate | Geographic logic: `venue.country = team.country` |
| **Q13** | 100+ Run Batting Partnerships | Intermediate | Partnership stands, inning tracking |
| **Q14** | Venue Bowling Dynamics | Intermediate | Multi-criteria grouping, economy ranking |
| **Q15** | Clutch Close-Match Performers | Intermediate | High-pressure margin filtering (`<50 runs / <5 wkts`) |
| **Q16** | Year-on-Year Batting Evolution | Intermediate | Annual progression tracking since 2020 |
| **Q17** | Toss Win Advantage % | Advanced | Win rate conversion grouped by bat/bowl decision |
| **Q18** | Economical Limited-Overs Bowlers | Advanced | White-ball economy rates with qualification barriers |
| **Q19** | Batting Consistency & Standard Deviation | Advanced | Statistical variance `SQRT(AVG(X²) - AVG(X)²)` |
| **Q20** | Format Workload & Batting Averages | Advanced | Cross-format match frequency and averages |
| **Q21** | Weighted Composite Player Ranking | Advanced | Algorithmic composite points formula (Bat/Bowl/Field) |
| **Q22** | Head-to-Head Prediction Analysis | Advanced | Symmetrical pair matching and margin differentials |
| **Q23** | Recent Form & Momentum Tracking | Advanced | `ROW_NUMBER() OVER (PARTITION BY ...)` ranking |
| **Q24** | Partnership Synergy & Success Rate | Advanced | Stand conversion percentages |
| **Q25** | Quarterly Career Trajectory | Advanced | `LAG()` window function, momentum classification |

---

## 🚀 Quickstart & Installation

### 1. Clone or Open Project Directory
```bash
cd C:\Users\DELL\.gemini\antigravity\scratch\cricbuzz_livestats
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Configure RapidAPI Key
Create a `.env` file or copy from `.env.example`:
```env
RAPIDAPI_KEY=your_key_here
RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com
```
*Note: If no API key is provided, the application runs seamlessly in offline simulation mode.*

### 4. Run the Application
```bash
streamlit run app.py
```

### 5. Run Automated Tests
```bash
pytest tests/
```

---

## 📂 Project Structure

```text
cricbuzz_livestats/
├── app.py                      # Master Streamlit entrance & landing page
├── config.py                   # Centralized configuration settings
├── requirements.txt            # Package dependencies
├── .env.example                # Sample environment variables
├── README.md                   # Complete documentation
│
├── api/                        # Cricbuzz API ingestion layer
│   ├── endpoints.py            # API URL mapping
│   └── cricbuzz_client.py      # Requests client with offline fallback
│
├── database/                   # 3NF Relational Database Layer
│   ├── schema.sql              # Normalized DDL (9 tables + indexes)
│   ├── seed_data.sql           # Realistic cricket dataset for all 25 queries
│   ├── connection.py           # Thread-safe connection pool & auto-init
│   └── crud_operations.py      # Parameterized CRUD transactions
│
├── sql/                        # SQL Analytics Engine
│   ├── beginner_queries.sql    # Queries 1 to 8
│   ├── intermediate_queries.sql# Queries 9 to 16
│   ├── advanced_queries.sql    # Queries 17 to 25
│   └── query_registry.py       # Query dictionary with metadata & SQL
│
├── utils/                      # Helper & charting utilities
│   ├── visualizer.py           # Interactive Plotly charts
│   └── formatters.py           # Metric badges & cards
│
├── pages/                      # Multi-page Streamlit views
│   ├── 1_🏠_Home.py
│   ├── 2_⚡_Live_Matches.py
│   ├── 3_📊_Top_Player_Stats.py
│   ├── 4_🔍_SQL_Analytics.py
│   └── 5_🛠️_CRUD_Operations.py
│
└── tests/                      # Automated test suite
    ├── test_database.py
    ├── test_queries.py
    └── test_api.py
```

---

## ⚖️ License
This project is licensed under the MIT License.
