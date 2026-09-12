# 🎬 Cricbuzz LiveStats: Project Demo Video Script

**Target Duration:** 6 – 8 Minutes  
**Audience:** Evaluators, Mentors, Technical Recruiters, Project Reviewers  
**Theme:** Real-Time Sports Analytics, Normalized 3NF SQL Database, Streamlit UI, and 25 Business Queries  

---

## 🛠️ Recording Setup & Pre-Flight Checklist

1. **Launch the Dashboard**:
   ```bash
   cd C:\Users\DELL\.gemini\antigravity\scratch\cricbuzz_livestats
   python -m streamlit run app.py
   ```
2. **Browser Setup**:
   - Open Chrome or Edge at `http://localhost:8501`.
   - Press `F11` (or zoom to 100%) for a clean full-screen view.
   - Close all unrelated browser tabs and silence system notifications.
3. **Recording Software**:
   - Free tools: **OBS Studio**, **Loom**, or **Windows Snipping Tool / Xbox Game Bar** (`Win + G` / `Win + Alt + R`).
   - Resolution: 1080p (1920x1080) at 30 or 60 FPS.
   - Audio: Test microphone input for crisp voice clarity.

---

## ⏱️ Video Timeline & Scene-by-Scene Script

---

### Scene 1: Introduction & Project Overview (0:00 - 0:45)
**Screen Display:** Landing page (`app.py`) showing the Hero Banner, KPI cards (6 Teams, 10 Venues, 34 Players, 35 Matches, 25 Queries), and Tech Stack badges.  
**Cursor Movement:** Hover smoothly over the KPI cards.

> **Voice-over:**  
> "Hello everyone! Welcome to the demonstration of **Cricbuzz LiveStats: Real-Time Cricket Insights & SQL-Based Analytics**.  
>  
> Cricket is one of the world's most data-rich sports, but broadcasters, fantasy platforms, and analysts often face fragmented data, lack of real-time pipeline integration, and difficulty querying complex historical relationships.  
>  
> To solve this, I designed and built this production-grade, end-to-end analytics platform. It combines real-time cricket data from the **Cricbuzz REST API**, a **3NF normalized relational database**, an analytics engine executing **25 advanced SQL business queries**, and an interactive multi-page **Streamlit dashboard** complete with administrative CRUD capabilities.  
>  
> Let's dive straight into how the system is engineered."

---

### Scene 2: System Architecture & Relational Database (0:45 - 1:45)
**Screen Display:** Navigate to **`1 🏠 Home`** page.  
**Action:** Click the **Architecture Overview** tab, scroll to the architecture diagram, then click the **Relational Schema (3NF)** tab.

> **Voice-over:**  
> "On our Home page, we have a complete overview of the multi-tier application architecture.  
>  
> We have cleanly decoupled our application into:  
> 1. A **Streamlit Presentation Layer**,  
> 2. A resilient **API Ingestion Client**,  
> 3. An analytical **SQL Engine**, and  
> 4. A **Thread-Safe Data Persistence Controller**.  
>  
> Moving to the Relational Schema tab: to satisfy intricate sports analytics queries—like consecutive batting partnerships, venue dynamics, and multi-format player comparisons—I structured our database into **9 normalized 3NF tables**:  
> - `teams`, `venues`, and `players` for core entities,  
> - `series` and `matches` capturing match-level context, toss decisions, and victory margins,  
> - And granular performance tables: `player_match_batting`, `player_match_bowling`, `player_match_fielding`, and `batting_partnerships`.  
>  
> All tables feature primary keys, cascading foreign key constraints, and B-tree indexes on frequently queried fields for sub-millisecond query performance."

---

### Scene 3: Live Match Center & API Resilience (1:45 - 3:00)
**Screen Display:** Click on **`2 ⚡ Live Matches`** in the sidebar.  
**Action:** Show the match dropdown (India vs Australia 3rd T20I), scroll down to the Batting Card, Bowling Figures, and Ball-by-Ball Commentary. Click the **Refresh Feed** button.

> **Voice-over:**  
> "Next, let's explore the **Live Match Center**.  
>  
> This module interacts directly with the **Cricbuzz REST API** using Python's `requests` library. We implemented automated timeout handling, header injection, and response parsing.  
>  
> Notice the resilience built into this client: if no RapidAPI key is configured or if network latency occurs, the client automatically switches to a high-fidelity offline simulation mode. This ensures stakeholders can test and evaluate the system anytime without API quota exhaustion.  
>  
> Looking at the scorecard for the ongoing 3rd T20I between India and Australia:  
> - We can see real-time match status: *'India need 24 runs in 18 balls to win'*.  
> - We have active run rates and target calculations.  
> - The live batting table shows runs, balls faced, strike rates, and boundaries.  
> - The bowling card tracks economy rates and wickets.  
> - And on the right, we have a live over-by-over commentary feed with boundaries dynamically color-coded—blue for sixes and green for fours."

---

### Scene 4: Top Player Statistics & Head-to-Head Comparison (3:00 - 4:15)
**Screen Display:** Click on **`3 📊 Top Player Stats`**.  
**Action:** Switch the format dropdown between `ODI` and `T20I`. Switch tabs between `Top Batsmen` and `Top Bowlers`. Then open the **Player Comparison** tab and select *Virat Kohli* vs *Steve Smith*.

> **Voice-over:**  
> "Moving to the **Top Player Statistics** module.  
>  
> Here, users can dynamically filter stats across formats: Test, ODI, or T20I.  
> - In the **Top Batsmen** tab, our SQL backend computes runs, batting averages, strike rates, centuries, and fifties on the fly, paired with an interactive Plotly bar chart.  
> - In the **Top Bowlers** tab, we aggregate wickets, maidens, and economy figures.  
>  
> A standout feature here is our **Head-to-Head Comparison** engine. When we select two players—for example, Virat Kohli and Steve Smith—the system instantly queries and aggregates their cross-format numbers side-by-side, rendering a comparative grouped bar chart analyzing total runs versus strike rates."

---

### Scene 5: SQL Analytics Engine (All 25 Business Queries) (4:15 - 6:00)
**Screen Display:** Click on **`4 🔍 SQL Analytics`**.  
**Action:**  
1. Select **Beginner (1-8)**: Pick **Q04: Venues with Capacity > 50,000**. Click `⚡ Execute Query`. Point to execution time. Show bar chart.  
2. Select **Intermediate (9-16)**: Pick **Q15: Clutch Performers in Close Matches**. Click `⚡ Execute Query`. Show table and chart.  
3. Select **Advanced (17-25)**: Pick **Q21: Weighted Composite Player Ranking Formula**. Expand the SQL syntax. Click `⚡ Execute Query`. Show the composite score ranking table.  
4. Optionally show **Q23: Form & Momentum Tracking** or **Q25: Quarterly Career Trajectory**.  
5. Click the **Download CSV** button.

> **Voice-over:**  
> "Now, let's look at the core analytical engine of this project: the **SQL Analytics Module**.  
>  
> The project specifications required solving **25 real-world cricket business queries**, categorized into Beginner, Intermediate, and Advanced tiers. I implemented a centralized query catalog with syntax inspection, live database execution, a latency performance timer, and dynamic Plotly visualizations.  
>  
> Let's test a few:  
> - Under **Beginner**, let's look at **Question 4: Venues with Capacity > 50,000**. Executing it takes under 5 milliseconds! Narendra Modi Stadium and Melbourne Cricket Ground top the chart.  
>  
> - Under **Intermediate**, let's inspect **Question 15: Clutch Performers in Close Matches**. This query isolates high-pressure finishes decided by fewer than 50 runs or 5 wickets, calculating player scoring averages and match win conversion when batting.  
>  
> - And under **Advanced**, here is **Question 21: Weighted Composite Player Ranking Formula**.  
>   Notice the SQL architecture here: we use three **Common Table Expressions (CTEs)** to independently aggregate batting, bowling, and fielding points based on weighted analytical formulas:  
>   - Batting: Runs × 0.01 + Avg × 0.5 + Strike Rate × 0.3  
>   - Bowling: Wickets × 2 + (50 - Avg) × 0.5 + (6 - Econ) × 2  
>   - Fielding: Catches × 3 + Stumpings × 5  
>   When we click Execute, the system ranks all international players in a single unified leaderboard!  
>  
> We can also inspect **Question 23**, which uses the `ROW_NUMBER() OVER (PARTITION BY ...)` window function to track recent form momentum, and **Question 25**, which applies `LAG()` for quarterly career trajectory analysis.  
>  
> Users can also export any query result directly with the **Download CSV** button."

---

### Scene 6: CRUD Operations & Data Governance (6:00 - 7:00)
**Screen Display:** Click on **`5 🛠️ CRUD Operations`**.  
**Action:**  
1. In **View Players**: Search 'Rohit' or filter by 'All-rounder'.  
2. In **Add Player**: Fill in sample cricketer: Name: *'Yashasvi Jaiswal'*, Team: *'India'*, Role: *'Batsman'*, Batting: *'Left-hand bat'*, Bowling: *'Right-arm legbreak'*, Debut: *2023*. Click **Create Player Record**. Show the green success toast!  
3. Show the **Record Match** tab.

> **Voice-over:**  
> "A production analytics system also requires robust data governance. Our **CRUD Operations** module allows administrators to manage cricket records through an intuitive, validated interface without writing raw SQL.  
>  
> - In **View Players**, we have real-time keyword search and team/role filters.  
> - In **Add Player**, let's register a new player—Yashasvi Jaiswal representing India. Upon submission, the form validates inputs, executes a parameterized SQL INSERT, and assigns a new player ID.  
> - We also have full **Edit** and **Delete** capabilities with confirmation safety checks to prevent accidental deletions.  
> - And in **Record Match**, tournament coordinators can submit completed match outcomes, toss decisions, and victory margins."

---

### Scene 7: Code Quality & Automated Test Suite (7:00 - 7:45)
**Screen Display:** Switch briefly to Terminal / IDE showing `tests/run_all_tests.py`.  
**Action:** Run `python tests/run_all_tests.py` in the terminal and let the 100% green pass results appear.

> **Voice-over:**  
> "Behind the user interface is clean, modular, PEP 8-compliant Python code.  
>  
> To guarantee stability, I created an automated test suite. Let's run `python tests/run_all_tests.py`:  
> - It verifies database initialization and relational entity counts,  
> - Tests the complete CRUD player lifecycle,  
> - Validates API ingestion and fallback payloads, and  
> - Automatically runs **all 25 SQL queries**, asserting non-empty, error-free results across every single question.  
>  
> As you can see, all 25 queries and unit tests passed with 100% success!"

---

### Scene 8: Conclusion & Wrap-Up (7:45 - 8:15)
**Screen Display:** Switch back to the Streamlit Home Page.  
**Action:** Scroll smoothly back to the top banner.

> **Voice-over:**  
> "To summarize: **Cricbuzz LiveStats** delivers an end-to-end cricket analytics platform—from real-time REST API consumption and normalized 3NF database architecture to complex window-function SQL queries and a multi-page interactive Streamlit web dashboard.  
>  
> The codebase is fully modular, documented with a detailed README, and ready for deployment.  
>  
> Thank you for your time and for watching this demonstration!"

---

## 💡 Top 5 Tips for a High-Scoring Presentation

1. **Speak with Steady Pace**: Don't rush through the SQL explanations; emphasize the business value (e.g. why fantasy leagues or broadcasters need these metrics).
2. **Smooth Cursor Movement**: Move your mouse deliberately to guide the viewer's eyes. Avoid shaking or erratically moving the cursor.
3. **Highlight the Execution Time**: When clicking *Execute Query* in SQL Analytics, point out the sub-10ms latency to showcase database indexing performance.
4. **Showcase Error Handling & Fallback**: Mention that the app never crashes even without an API key because of the fallback architecture.
5. **Keep Streamlit Server Running**: Start the server before you begin recording so there are no loading delays.
