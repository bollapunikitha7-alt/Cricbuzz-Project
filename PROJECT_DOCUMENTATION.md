# 🏏 Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics
## Comprehensive Technical Project Report & Submission Documentation

---

### 📄 Executive Summary

* **Project Title:** Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics
* **Domain:** Sports Analytics, Data Engineering, and Full-Stack Data Applications
* **Core Technologies:** Python 3.10+, SQLite (Normalized 3NF), Streamlit, REST APIs (Cricbuzz RapidAPI), Pandas, Plotly Express
* **Application URL (Local):** `http://localhost:8501`
* **Repository / Directory:** `C:\Users\DELL\.gemini\antigravity\scratch\cricbuzz_livestats`

**Cricbuzz LiveStats** is an enterprise-grade sports analytics platform designed to bridge the gap between real-time cricket match feeds and deep historical relational querying. Built around a normalized Third Normal Form (3NF) relational database, an automated Cricbuzz REST API ingestion client with offline simulation fallback, and an interactive multi-page Streamlit web dashboard, the system solves **25 real-world cricket business analytics queries** across Beginner, Intermediate, and Advanced tiers.

---

## 1. 🎯 Problem Statement & Business Objectives

### 1.1 The Industry Problem
Modern cricket generates voluminous, multi-dimensional data across ball-by-ball actions, player form, pitch conditions, and tournament series. Despite this data abundance, sports broadcasters, media outlets, and fantasy platforms face three critical bottlenecks:
1. **Data Fragmentation**: Live match data exists in volatile JSON feeds, while historical analytics require persistent structured storage.
2. **Analytical Latency**: Real-time broadcast commentary and fantasy selections require immediate evaluation of complex statistical metrics (e.g., clutch match performance, consecutive batting partnership synergy, quarterly momentum trajectories).
3. **Data Governance & Integrity**: Non-technical administrators lack safe, validated interfaces to inspect, update, or append match records without direct database console manipulation.

### 1.2 Project Objectives
* **Real-Time Data Ingestion**: Ingest live match updates, scorecards, and commentary feeds via Cricbuzz REST APIs with automatic fallback resilience.
* **3NF Relational Data Modeling**: Architect a normalized 9-table schema enforcing referential integrity and performance indexing.
* **Complex SQL Analytics**: Formulate and optimize 25 production-ready SQL queries utilizing subqueries, conditional aggregations, Common Table Expressions (CTEs), and Window Functions (`ROW_NUMBER()`, `LAG()`).
* **Interactive Visualization Dashboard**: Develop a 5-page Streamlit web application providing intuitive data exploration, dynamic Plotly visualizers, and tabular CSV exports.
* **Administrative Data Governance (CRUD)**: Provide full form-based Create, Read, Update, and Delete operations protected against SQL injection attacks.

---

## 2. 🏛️ System Architecture

The application adopts a **Decoupled Multi-Tier Architecture** separating the presentation layer from business logic, data persistence, and external API services:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       STREAMLIT PRESENTATION LAYER                          │
│   [Home: 1_🏠]   [Live: 2_⚡]   [Stats: 3_📊]   [SQL: 4_🔍]   [CRUD: 5_🛠️]    │
└───────────────────────┬───────────────────────────────┬─────────────────────┘
                        │                               │
                        ▼                               ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────┐
│           API CLIENT LAYER            │ │        SQL ANALYTICS ENGINE       │
│  - Cricbuzz RapidAPI Client           │ │  - 25 Query Catalog               │
│  - Automated Timeout & Retry Handling │ │  - Window Functions & CTEs        │
│  - Offline Simulation Fallback Engine │ │  - Query Performance Timer (ms)   │
└───────────────────────┬───────────────┘ └─────────────┬─────────────────────┘
                        │                               │
                        ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DATA PERSISTENCE & CRUD LAYER                          │
│   - Thread-Safe SQLite Connection Pool                                      │
│   - Parameterized SQL Execution (Zero SQL Injection)                        │
│   - Normalized 3NF Relational Schema (9 Tables + B-Tree Indexes)            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. 🗄️ Relational Database Design (Normalized 3NF)

To eliminate update anomalies and prevent redundant storage of repetitive match attributes, the database is normalized to **Third Normal Form (3NF)**.

### 3.1 Entity Relationship Overview
The database comprises **9 relational entities**:
1. **`teams`**: Core international teams and country affiliations.
2. **`venues`**: Stadium metadata, locations, and spectator capacities.
3. **`players`**: Player profiles, playing roles, batting/bowling styles, and debut years.
4. **`series`**: International tournaments, host nations, and scheduled formats.
5. **`matches`**: Fixture records, dates, venues, toss decisions, winners, and victory margins.
6. **`player_match_batting`**: Granular innings batting statistics (runs, balls, 4s, 6s, strike rate, out status).
7. **`player_match_bowling`**: Granular innings bowling figures (overs, maidens, runs conceded, wickets, economy).
8. **`player_match_fielding`**: Catches, stumpings, and run-outs per match.
9. **`batting_partnerships`**: Consecutive batting stands, partnership runs, and wicket numbers.

### 3.2 Data Dictionary

| Table Name | Column Name | Data Type | Constraint | Description |
| :--- | :--- | :--- | :--- | :--- |
| **teams** | `team_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique team identifier |
| | `team_name` | VARCHAR(50) | NOT NULL, UNIQUE | Full team name (e.g. India) |
| | `short_code` | VARCHAR(10) | NOT NULL, UNIQUE | 3-letter abbreviation (e.g. IND) |
| | `country` | VARCHAR(50) | NOT NULL | Sovereign nation of team |
| **venues** | `venue_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique stadium identifier |
| | `venue_name` | VARCHAR(100) | NOT NULL | Stadium title |
| | `city` | VARCHAR(50) | NOT NULL | Host city |
| | `country` | VARCHAR(50) | NOT NULL | Host country |
| | `capacity` | INTEGER | NOT NULL | Spectator seating capacity |
| **players** | `player_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique player identifier |
| | `full_name` | VARCHAR(100) | NOT NULL | Player full name |
| | `team_id` | INTEGER | FOREIGN KEY -> teams(team_id) | Associated national squad |
| | `playing_role` | VARCHAR(50) | NOT NULL | Batsman, Bowler, All-rounder, WK |
| | `batting_style`| VARCHAR(50) | NOT NULL | Right-hand / Left-hand bat |
| | `bowling_style`| VARCHAR(50) | NOT NULL | Bowling action / delivery type |
| | `debut_year` | INTEGER | CHECK (debut_year >= 1990) | International debut year |
| **matches** | `match_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique match identifier |
| | `series_id` | INTEGER | FOREIGN KEY -> series(series_id)| Parent tournament series |
| | `match_desc` | VARCHAR(150) | NOT NULL | Match description |
| | `team1_id` | INTEGER | FOREIGN KEY -> teams(team_id) | First participating team |
| | `team2_id` | INTEGER | FOREIGN KEY -> teams(team_id) | Second participating team |
| | `venue_id` | INTEGER | FOREIGN KEY -> venues(venue_id) | Match venue |
| | `match_date` | DATE | NOT NULL | Scheduled match date |
| | `match_format`| VARCHAR(20) | NOT NULL | Test, ODI, or T20I |
| | `toss_winner_id`| INTEGER | FOREIGN KEY -> teams(team_id) | Team winning the coin toss |
| | `toss_decision`| VARCHAR(10) | NOT NULL ('bat' or 'bowl') | Choice made upon winning toss |
| | `match_winner_id`| INTEGER| FOREIGN KEY -> teams(team_id) | Winning team |
| | `win_margin` | INTEGER | NOT NULL | Margin of victory |
| | `win_type` | VARCHAR(20) | NOT NULL ('runs' or 'wickets')| Metric of victory |

### 3.3 Database Indexing Strategy
To optimize analytical execution times, B-Tree indexes were constructed on all primary join paths:
* `idx_players_team` ON `players(team_id)`
* `idx_matches_date` ON `matches(match_date)`
* `idx_matches_format` ON `matches(match_format)`
* `idx_batting_player` ON `player_match_batting(player_id)`
* `idx_bowling_player` ON `player_match_bowling(player_id)`
* `idx_partnerships_match` ON `batting_partnerships(match_id)`

---

## 4. 🌐 REST API Integration & Fallback Resilience

The ingestion layer (`api/cricbuzz_client.py`) is engineered to interface with the official **RapidAPI Cricbuzz Endpoints**:
* `GET /matches/v1/live`: Live international match summaries.
* `GET /mcenter/v1/{match_id}/scard`: Comprehensive scorecard details.
* `GET /mcenter/v1/{match_id}/comm`: Over-by-over ball commentary.

### Fallback Simulation Architecture
External sports APIs frequently introduce strict rate quotas, subscription requirements, or connection timeouts. To guarantee that evaluators and end-users experience zero application crashes, `CricbuzzClient` implements **Graceful Degradation**:
1. It inspects whether `RAPIDAPI_KEY` is present and valid.
2. If absent or if an HTTP exception (e.g. 429 Rate Limit, 504 Gateway Timeout) occurs, it automatically routes requests to an internal high-fidelity mock engine.
3. The mock engine supplies full realistic scorecards (e.g. India vs Australia 3rd T20I thriller in Ahmedabad, England vs South Africa 2nd ODI) complete with current batsmen, bowlers, and live commentary.

---

## 5. 🧮 25 SQL Analytical Queries Catalog

All 25 business practice queries were verified against the relational schema. Below is the complete specification across tiers:

### 5.1 Beginner Level (Questions 1 – 8)
* **Q1: Indian Players Profile**
  * *Concepts:* `SELECT`, `JOIN`, `WHERE`, `ORDER BY`
  * *Objective:* Extract name, role, batting style, and bowling style for Indian squad members.
* **Q2: Recent Matches (30-Day Window)**
  * *Concepts:* `julianday()`, date filtering, multi-table `JOIN`
  * *Objective:* Chronologically list fixtures completed within the last 30 days.
* **Q3: Top 10 Highest Run Scorers in ODI Cricket**
  * *Concepts:* `SUM()`, `AVG()`, `COUNT(CASE WHEN)`, `GROUP BY`
  * *Objective:* Rank 50-over run scorers with batting average and century counts.
* **Q4: Venues with Seating Capacity > 50,000**
  * *Concepts:* Numeric inequality filtering, `ORDER BY capacity DESC`
  * *Objective:* Identify mega-venues capable of hosting high-revenue marquee finals.
* **Q5: Total Matches Won per Team**
  * *Concepts:* `COUNT()`, `GROUP BY`, `ORDER BY DESC`
  * *Objective:* Calculate cumulative all-time wins per nation.
* **Q6: Squad Distribution by Playing Role**
  * *Concepts:* Categorical aggregation, `COUNT()`
  * *Objective:* Determine squad balance across Batsmen, Bowlers, All-rounders, and Wicket-keepers.
* **Q7: Highest Individual Score per Format**
  * *Concepts:* `MAX()`, `GROUP BY match_format`
  * *Objective:* Discover format-specific peak individual batting innings (Test, ODI, T20I).
* **Q8: International Series Starting in 2024**
  * *Concepts:* `strftime('%Y', start_date) = '2024'`
  * *Objective:* Audit tournament schedules launched during the 2024 calendar year.

### 5.2 Intermediate Level (Questions 9 – 16)
* **Q9: Multi-Format Impact of All-Rounders**
  * *Concepts:* Multi-table `JOIN`, `COALESCE()`, `HAVING`
  * *Objective:* Filter all-rounders contributing runs and wickets across different formats.
* **Q10: Last 20 Completed Matches & Victory Margins**
  * *Concepts:* Dual team `JOIN`, `LIMIT 20`, string concatenation
  * *Objective:* Audit recent match results with margins and victory types.
* **Q11: Cross-Format Adaptability Comparison**
  * *Concepts:* Conditional aggregation `SUM(CASE WHEN ...)`, `HAVING COUNT(DISTINCT) >= 2`
  * *Objective:* Compare batting runs in Test, ODI, and T20I alongside overall career average.
* **Q12: Home vs Away Performance Analysis**
  * *Concepts:* Geographic condition matching (`venue.country = team.country`), `SUM(CASE)`
  * *Objective:* Measure home advantage win rates against away match dominance.
* **Q13: Consecutive Batting Partnerships >= 100 Runs**
  * *Concepts:* Double player table `JOIN`, partnership thresholds
  * *Objective:* Identify match-defining century stands between consecutive batting positions.
* **Q14: Venue Bowling Performance Dynamics**
  * *Concepts:* Venue grouping, bowling economy calculation, threshold filtering
  * *Objective:* Evaluate bowler economy rates across grounds with >= 2 matches and >= 4 overs.
* **Q15: Clutch Performers in Close Matches**
  * *Concepts:* Margin filtering (`< 50 runs` OR `< 5 wickets`), scoring averages
  * *Objective:* Identify batsmen who deliver match-winning runs under high pressure finishes.
* **Q16: Annual Batting Progression (2020+)**
  * *Concepts:* Date extraction `strftime('%Y')`, multi-year grouping
  * *Objective:* Track year-on-year scoring volume and strike rate evolution.

### 5.3 Advanced Level (Questions 17 – 25)
* **Q17: Toss Decision Win Advantage Analysis**
  * *Concepts:* Percentage calculation, conditional conversion
  * *Objective:* Correlate winning the toss and choosing to bat or bowl with final match victory.
* **Q18: Most Economical Limited-Overs Bowlers**
  * *Concepts:* In-list filtering `('ODI', 'T20I')`, average qualification criteria
  * *Objective:* Rank white-ball containment bowlers with lowest runs conceded per over.
* **Q19: Batting Consistency & Standard Deviation**
  * *Concepts:* Mathematical variance `SQRT(AVG(X²) - AVG(X)²)`
  * *Objective:* Evaluate scoring stability vs volatility for players with >= 10 balls faced.
* **Q20: Multi-Format Workload Distribution**
  * *Concepts:* Format-specific match counts, aggregate averages
  * *Objective:* Profile all-format match volume and format-wise averages.
* **Q21: Weighted Composite Player Ranking Formula**
  * *Concepts:* Multiple Common Table Expressions (CTEs), weighted scoring algorithm
  * *Formula:*
    * Batting Points: `Runs * 0.01 + Avg * 0.5 + SR * 0.3`
    * Bowling Points: `Wickets * 2 + (50 - Avg) * 0.5 + (6 - Econ) * 2`
    * Fielding Points: `Catches * 3 + Stumpings * 5`
  * *Objective:* Synthesize all-round performance into a single objective score.
* **Q22: Head-to-Head Match Prediction Analytics**
  * *Concepts:* Symmetrical pair matching, win percentage ratios
  * *Objective:* Quantify historical dominance and average victory margins between rival nations.
* **Q23: Recent Form & Momentum Tracking**
  * *Concepts:* Window Function `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY match_date DESC)`
  * *Objective:* Classify players into 'Excellent', 'Good', 'Average', or 'Poor' form using rolling last 5 vs last 10 innings.
* **Q24: Batting Partnership Synergy & Conversion Rate**
  * *Concepts:* Pair grouping, 50+ conversion percentage
  * *Objective:* Measure chemistry and success rate of regular batting pairs.
* **Q25: Quarterly Career Trajectory Time-Series**
  * *Concepts:* Window Function `LAG() OVER (...)`, quarterly time-series grouping
  * *Objective:* Measure quarter-over-quarter momentum to classify career phases: 'Career Ascending', 'Career Declining', or 'Career Stable'.

---

## 6. 🖥️ Interactive Dashboard Implementation

The front-end is constructed using **Streamlit 1.30+** following clean UI/UX standards:
1. **`app.py`**: Central gateway with KPI cards, navigation sidebar, and database health metrics.
2. **`pages/1_🏠_Home.py`**: Architecture documentation, 3NF schema tables, and live database record counters.
3. **`pages/2_⚡_Live_Matches.py`**: Interactive match cards, live scorecards, run-rate pills, and over commentary.
4. **`pages/3_📊_Top_Player_Stats.py`**: Format filtering, leaderboards, and an interactive Head-to-Head player comparison tool.
5. **`pages/4_🔍_SQL_Analytics.py`**: Filter all 25 queries by difficulty, inspect syntax, execute live with performance timing (ms), render Plotly visualizations, and export CSVs.
6. **`pages/5_🛠️_CRUD_Operations.py`**: Validated administrative forms:
   - *Add Player*: Validates mandatory fields and assigns foreign keys.
   - *Search Players*: Dynamic multi-attribute filtering.
   - *Edit Player*: Pre-populates existing data for inline modifications.
   - *Delete Player*: Confirmation checkbox preventing unintended cascading deletions.
   - *Record Match*: Logs completed fixtures, venues, toss details, and margins.

---

## 7. ✅ Verification & Test Execution Report

The system includes an automated test runner (`tests/run_all_tests.py`):

```text
======================================================================
                  CRICBUZZ LIVESTATS TEST SUITE
======================================================================
=== 1. TESTING DATABASE & CRUD ===
Database Summary: {'teams': 6, 'venues': 10, 'players': 34, 'series': 8, 'matches': 35, 'player_match_batting': 89, 'player_match_bowling': 86}
Database & CRUD tests: PASS

=== 2. TESTING ALL 25 SQL QUERIES ===
PASS: Q01 [Beginner] (12 rows, 4 cols) - Indian Players Profile
PASS: Q02 [Beginner] (5 rows, 5 cols) - Recent Matches (Last 30 Days Window)
PASS: Q03 [Beginner] (10 rows, 4 cols) - Top 10 Highest Run Scorers in ODI Cricket
PASS: Q04 [Beginner] (4 rows, 4 cols) - Venues with Capacity > 50,000
PASS: Q05 [Beginner] (4 rows, 2 cols) - Match Wins per Team
PASS: Q06 [Beginner] (4 rows, 2 cols) - Player Count per Playing Role
PASS: Q07 [Beginner] (3 rows, 2 cols) - Highest Individual Batting Score per Format
PASS: Q08 [Beginner] (4 rows, 5 cols) - Series Started in 2024
PASS: Q09 [Intermediate] (7 rows, 4 cols) - All-Rounders Multi-Format Impact
PASS: Q10 [Intermediate] (20 rows, 7 cols) - Last 20 Completed Matches and Margins
PASS: Q11 [Intermediate] (14 rows, 5 cols) - Cross-Format Batting Performance Comparison
PASS: Q12 [Intermediate] (6 rows, 4 cols) - Home vs Away Win Analysis
PASS: Q13 [Intermediate] (10 rows, 5 cols) - Batting Partnerships >= 100 Runs
PASS: Q14 [Intermediate] (22 rows, 5 cols) - Venue Bowling Performance Dynamics
PASS: Q15 [Intermediate] (9 rows, 4 cols) - Clutch Performers in Close Matches
PASS: Q16 [Intermediate] (23 rows, 5 cols) - Year-on-Year Batting Evolution (2020+)
PASS: Q17 [Advanced] (2 rows, 4 cols) - Toss Decision Win Advantage Analysis
PASS: Q18 [Advanced] (8 rows, 4 cols) - Most Economical Limited-Overs Bowlers
PASS: Q19 [Advanced] (12 rows, 4 cols) - Batting Consistency & Standard Deviation
PASS: Q20 [Advanced] (13 rows, 8 cols) - Multi-Format Match Distribution & Averages
PASS: Q21 [Advanced] (34 rows, 6 cols) - Weighted Composite Player Ranking Formula
PASS: Q22 [Advanced] (4 rows, 9 cols) - Head-to-Head Match Prediction Analytics
PASS: Q23 [Advanced] (13 rows, 6 cols) - Recent Player Form & Momentum Tracking
PASS: Q24 [Advanced] (8 rows, 7 cols) - Batting Partnership Synergy & Success Rate
PASS: Q25 [Advanced] (18 rows, 5 cols) - Quarterly Time-Series Career Trajectory

All 25 SQL Queries: 100% PASS!

=== 3. TESTING API CLIENT & FALLBACK ===
API Client: PASS (3 live matches parsed, scorecard verified)

======================================================================
            ALL TESTS PASSED SUCCESSFULLY! (100% GREEN)
======================================================================
```

---

## 8. 🚀 Installation & Execution Guide

### Prerequisites
* Python 3.10 or higher
* Windows / macOS / Linux

### Step-by-Step Setup
1. **Navigate to the Project Root**:
   ```powershell
   cd C:\Users\DELL\.gemini\antigravity\scratch\cricbuzz_livestats
   ```
2. **Install Required Packages**:
   ```powershell
   pip install -r requirements.txt
   ```
3. **(Optional) Configure API Keys**:
   Create a `.env` file from `.env.example`:
   ```env
   RAPIDAPI_KEY=your_key_here
   RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com
   ```
4. **Launch the Dashboard**:
   ```powershell
   python -m streamlit run app.py
   ```
5. **Run the Automated Test Suite**:
   ```powershell
   python tests/run_all_tests.py
   ```

---

## 9. 🎓 Viva & Technical Interview Questions

### Q1: Why was Third Normal Form (3NF) selected over storing denormalized match summaries?
**Answer:** A denormalized approach leads to update and deletion anomalies. For example, if a player's batting style changes or a venue capacity is updated, it would have to be modified across hundreds of historical match rows. In 3NF, player and venue attributes reside strictly in their respective primary tables, linked via foreign keys. This guarantees consistency and reduces storage footprint.

### Q2: How did you compute Standard Deviation in Question 19 using pure SQLite?
**Answer:** While enterprise engines like PostgreSQL have built-in `STDDEV()` aggregates, SQLite lacks a native standard deviation function out of the box. We applied the mathematical identity:
$$\sigma = \sqrt{E[X^2] - (E[X])^2} = \sqrt{	ext{AVG}(X^2) - 	ext{AVG}(X)^2}$$
Using SQLite's built-in `SQRT()`, `AVG()`, and `MAX(0, ...)` to safeguard against negative floating-point epsilon rounding, we calculated exact standard deviations directly in SQL.

### Q3: How do the Window Functions in Question 23 and Question 25 work?
**Answer:** 
* In **Question 23 (Form Tracking)**, `ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY match_date DESC)` assigns sequential ranks to each player's batting performances chronologically. Filtering on `rn <= 5` vs `rn <= 10` isolates recent performances from broader samples to measure momentum.
* In **Question 25 (Career Trajectory)**, `LAG(avg_runs) OVER (PARTITION BY player_id ORDER BY quarter)` inspects the prior quarter's performance without requiring an expensive self-join, calculating immediate quarter-on-quarter differentials.

### Q4: How does the application handle API failures or missing API keys?
**Answer:** The `CricbuzzClient` implements a dual-mode pattern. Before invoking external network endpoints, it validates whether a valid key exists. If unconfigured or if a network exception/timeout occurs, it catches the error and serves realistic, pre-cached live match payloads. This pattern (Circuit Breaker / Graceful Degradation) guarantees that the user experience is never broken.

---

## 10. 🏁 Conclusion & Future Roadmap

The **Cricbuzz LiveStats** project fulfills all sports analytics requirements, demonstrating full-stack competencies in database normalization, SQL query optimization, REST API integration, and interactive web visualization.

### Future Improvements
1. **Predictive Machine Learning**: Integrate a Logistic Regression / XGBoost model predicting second-innings chase win probabilities based on current run rate and required run rate.
2. **Ball-by-Ball Hawkeye Mapping**: Incorporate pitch map coordinates and wagon wheel visualizations for individual batsman boundary profiles.
3. **Cloud Database Migration**: Deploy a cloud PostgreSQL instance on AWS RDS or Supabase with automated daily API cron ingestion jobs.

---
**Report Generated for Project Submission & Technical Assessment.**
