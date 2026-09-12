"""
Query Registry Module.
Defines metadata, problem statements, execution categories, and visualizations
for all 25 SQL practice questions.
"""

QUERIES = {
    1: {
        "title": "Indian Players Profile",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Identify national squad composition, batting handedness, and bowling options for India.",
        "sql": """SELECT 
    p.full_name, 
    p.playing_role, 
    p.batting_style, 
    p.bowling_style 
FROM players p 
JOIN teams t ON p.team_id = t.team_id 
WHERE t.team_name = 'India' 
ORDER BY p.full_name ASC;""",
        "chart_type": "pie",
        "chart_col": "playing_role",
        "chart_val": "full_name"
    },
    2: {
        "title": "Recent Matches (Last 30 Days Window)",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Display fixture recency and venues for media broadcast match tracking.",
        "sql": """SELECT 
    m.match_desc, 
    t1.team_name AS team1, 
    t2.team_name AS team2, 
    v.venue_name || ', ' || v.city AS venue, 
    m.match_date 
FROM matches m 
JOIN teams t1 ON m.team1_id = t1.team_id 
JOIN teams t2 ON m.team2_id = t2.team_id 
JOIN venues v ON m.venue_id = v.venue_id 
WHERE julianday((SELECT MAX(match_date) FROM matches)) - julianday(m.match_date) <= 30
ORDER BY m.match_date DESC;""",
        "chart_type": "table"
    },
    3: {
        "title": "Top 10 Highest Run Scorers in ODI Cricket",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Analyze top cumulative run scorers in 50-over cricket with batting averages and century tallies.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    SUM(b.runs_scored) AS total_runs, 
    ROUND(AVG(b.runs_scored), 2) AS batting_average, 
    COUNT(CASE WHEN b.runs_scored >= 100 THEN 1 END) AS centuries 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
WHERE m.match_format = 'ODI' 
GROUP BY p.player_id, p.full_name 
ORDER BY total_runs DESC 
LIMIT 10;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "total_runs"
    },
    4: {
        "title": "Venues with Capacity > 50,000",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Determine mega-stadium availability for high-revenue marquee matches and tournaments.",
        "sql": """SELECT 
    venue_name, 
    city, 
    country, 
    capacity 
FROM venues 
WHERE capacity > 50000 
ORDER BY capacity DESC;""",
        "chart_type": "bar",
        "x": "venue_name",
        "y": "capacity"
    },
    5: {
        "title": "Match Wins per Team",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Evaluate all-time international team win percentages and match dominance.",
        "sql": """SELECT 
    t.team_name, 
    COUNT(m.match_id) AS total_wins 
FROM teams t 
JOIN matches m ON t.team_id = m.match_winner_id 
GROUP BY t.team_id, t.team_name 
ORDER BY total_wins DESC;""",
        "chart_type": "bar",
        "x": "team_name",
        "y": "total_wins"
    },
    6: {
        "title": "Player Count per Playing Role",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Assess squad balance across Batsmen, Bowlers, All-rounders, and Wicket-keepers.",
        "sql": """SELECT 
    playing_role, 
    COUNT(player_id) AS player_count 
FROM players 
GROUP BY playing_role 
ORDER BY player_count DESC;""",
        "chart_type": "pie",
        "chart_col": "playing_role",
        "chart_val": "player_count"
    },
    7: {
        "title": "Highest Individual Batting Score per Format",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Track format-specific peak single-innings batting milestones (Test, ODI, T20I).",
        "sql": """SELECT 
    m.match_format, 
    MAX(b.runs_scored) AS highest_score 
FROM player_match_batting b 
JOIN matches m ON b.match_id = m.match_id 
GROUP BY m.match_format 
ORDER BY highest_score DESC;""",
        "chart_type": "bar",
        "x": "match_format",
        "y": "highest_score"
    },
    8: {
        "title": "Series Started in 2024",
        "category": "Beginner",
        "level": "Easy",
        "business_problem": "Review the 2024 international cricket calendar, venues, and match allocations.",
        "sql": """SELECT 
    series_name, 
    host_country, 
    match_type, 
    start_date, 
    total_matches 
FROM series 
WHERE strftime('%Y', start_date) = '2024' 
ORDER BY start_date ASC;""",
        "chart_type": "table"
    },
    9: {
        "title": "All-Rounders Multi-Format Impact",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Discover versatile all-rounders who contribute significantly with both bat and ball.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    m.match_format, 
    SUM(b.runs_scored) AS total_runs, 
    COALESCE(SUM(bw.wickets_taken), 0) AS total_wickets 
FROM players p 
JOIN player_match_batting b ON p.player_id = b.player_id 
JOIN matches m ON b.match_id = m.match_id 
LEFT JOIN player_match_bowling bw ON p.player_id = bw.player_id AND b.match_id = bw.match_id 
WHERE p.playing_role = 'All-rounder' 
GROUP BY p.player_id, p.full_name, m.match_format 
HAVING total_runs >= 50 OR total_wickets >= 2
ORDER BY total_runs DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "total_runs"
    },
    10: {
        "title": "Last 20 Completed Matches and Margins",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Provide a comprehensive audit of recent match outcomes, margins, and victorious teams.",
        "sql": """SELECT 
    m.match_desc, 
    t1.team_name AS team1, 
    t2.team_name AS team2, 
    tw.team_name AS winning_team, 
    m.win_margin || ' ' || m.win_type AS victory_margin, 
    m.win_type, 
    v.venue_name 
FROM matches m 
JOIN teams t1 ON m.team1_id = t1.team_id 
JOIN teams t2 ON m.team2_id = t2.team_id 
JOIN venues v ON m.venue_id = v.venue_id 
LEFT JOIN teams tw ON m.match_winner_id = tw.team_id 
WHERE m.match_status = 'Completed' 
ORDER BY m.match_date DESC 
LIMIT 20;""",
        "chart_type": "table"
    },
    11: {
        "title": "Cross-Format Batting Performance Comparison",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Compare player adaptability across Test, ODI, and T20I cricket formats.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    SUM(CASE WHEN m.match_format = 'Test' THEN b.runs_scored ELSE 0 END) AS test_runs, 
    SUM(CASE WHEN m.match_format = 'ODI' THEN b.runs_scored ELSE 0 END) AS odi_runs, 
    SUM(CASE WHEN m.match_format = 'T20I' THEN b.runs_scored ELSE 0 END) AS t20i_runs, 
    ROUND(AVG(b.runs_scored), 2) AS overall_batting_avg 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
GROUP BY p.player_id, p.full_name 
HAVING COUNT(DISTINCT m.match_format) >= 2 
ORDER BY overall_batting_avg DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "overall_batting_avg"
    },
    12: {
        "title": "Home vs Away Win Analysis",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Investigate home advantage by verifying if match venue matches team country.",
        "sql": """SELECT 
    t.team_name, 
    SUM(CASE WHEN v.country = t.country AND m.match_winner_id = t.team_id THEN 1 ELSE 0 END) AS home_wins, 
    SUM(CASE WHEN v.country != t.country AND m.match_winner_id = t.team_id THEN 1 ELSE 0 END) AS away_wins, 
    COUNT(CASE WHEN m.match_winner_id = t.team_id THEN 1 END) AS total_wins 
FROM teams t 
LEFT JOIN matches m ON t.team_id = m.team1_id OR t.team_id = m.team2_id 
LEFT JOIN venues v ON m.venue_id = v.venue_id 
GROUP BY t.team_id, t.team_name 
ORDER BY total_wins DESC;""",
        "chart_type": "grouped_bar",
        "x": "team_name",
        "y1": "home_wins",
        "y2": "away_wins"
    },
    13: {
        "title": "Batting Partnerships >= 100 Runs",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Find marathon consecutive-batsmen stands that pivoted match results.",
        "sql": """SELECT 
    p1.full_name AS batsman1, 
    p2.full_name AS batsman2, 
    bp.partnership_runs, 
    bp.innings, 
    m.match_desc 
FROM batting_partnerships bp 
JOIN players p1 ON bp.batsman1_id = p1.player_id 
JOIN players p2 ON bp.batsman2_id = p2.player_id 
JOIN matches m ON bp.match_id = m.match_id 
WHERE bp.partnership_runs >= 100 
ORDER BY bp.partnership_runs DESC;""",
        "chart_type": "bar",
        "x": "batsman1",
        "y": "partnership_runs"
    },
    14: {
        "title": "Venue Bowling Performance Dynamics",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Evaluate bowler effectiveness and economy rates across specific international venues.",
        "sql": """SELECT 
    p.full_name AS bowler_name, 
    v.venue_name, 
    COUNT(DISTINCT pb.match_id) AS matches_played, 
    ROUND(AVG(pb.economy_rate), 2) AS avg_economy, 
    SUM(pb.wickets_taken) AS total_wickets 
FROM player_match_bowling pb 
JOIN players p ON pb.player_id = p.player_id 
JOIN matches m ON pb.match_id = m.match_id 
JOIN venues v ON m.venue_id = v.venue_id 
WHERE pb.overs_bowled >= 4.0 
GROUP BY p.player_id, v.venue_id, p.full_name, v.venue_name 
HAVING COUNT(DISTINCT pb.match_id) >= 2 
ORDER BY total_wickets DESC, avg_economy ASC;""",
        "chart_type": "scatter",
        "x": "avg_economy",
        "y": "total_wickets"
    },
    15: {
        "title": "Clutch Performers in Close Matches",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Identify batsmen who deliver match-winning runs under high-pressure finishes (<50 runs or <5 wkts).",
        "sql": """SELECT 
    p.full_name AS player_name, 
    COUNT(DISTINCT m.match_id) AS close_matches_played, 
    ROUND(AVG(b.runs_scored), 2) AS avg_runs, 
    SUM(CASE WHEN m.match_winner_id = p.team_id THEN 1 ELSE 0 END) AS close_matches_won 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
WHERE (m.win_type = 'runs' AND m.win_margin < 50) 
   OR (m.win_type = 'wickets' AND m.win_margin < 5) 
GROUP BY p.player_id, p.full_name 
HAVING COUNT(DISTINCT m.match_id) >= 2 
ORDER BY avg_runs DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "avg_runs"
    },
    16: {
        "title": "Year-on-Year Batting Evolution (2020+)",
        "category": "Intermediate",
        "level": "Medium",
        "business_problem": "Track annual progression in scoring volume and strike rates for key batsmen.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    strftime('%Y', m.match_date) AS match_year, 
    ROUND(AVG(b.runs_scored), 2) AS avg_runs_per_match, 
    ROUND(AVG(b.strike_rate), 2) AS avg_strike_rate, 
    COUNT(DISTINCT m.match_id) AS matches_played 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
WHERE m.match_date >= '2020-01-01' 
GROUP BY p.player_id, p.full_name, match_year 
HAVING COUNT(DISTINCT m.match_id) >= 2 
ORDER BY p.full_name, match_year ASC;""",
        "chart_type": "line",
        "x": "match_year",
        "y": "avg_runs_per_match"
    },
    17: {
        "title": "Toss Decision Win Advantage Analysis",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Determine statistical correlation between winning the toss, electing to bat/bowl, and match victory.",
        "sql": """SELECT 
    toss_decision, 
    COUNT(*) AS total_matches, 
    SUM(CASE WHEN toss_winner_id = match_winner_id THEN 1 ELSE 0 END) AS matches_won, 
    ROUND(100.0 * SUM(CASE WHEN toss_winner_id = match_winner_id THEN 1 ELSE 0 END) / COUNT(*), 2) AS win_percentage 
FROM matches 
WHERE match_winner_id IS NOT NULL 
GROUP BY toss_decision;""",
        "chart_type": "pie",
        "chart_col": "toss_decision",
        "chart_val": "matches_won"
    },
    18: {
        "title": "Most Economical Limited-Overs Bowlers",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Identify containment bowlers in white-ball cricket (ODI/T20I) with lowest runs conceded per over.",
        "sql": """SELECT 
    p.full_name AS bowler_name, 
    COUNT(DISTINCT pb.match_id) AS matches_bowled, 
    ROUND(AVG(pb.economy_rate), 2) AS overall_economy, 
    SUM(pb.wickets_taken) AS total_wickets 
FROM player_match_bowling pb 
JOIN players p ON pb.player_id = p.player_id 
JOIN matches m ON pb.match_id = m.match_id 
WHERE m.match_format IN ('ODI', 'T20I') 
GROUP BY p.player_id, p.full_name 
HAVING COUNT(DISTINCT pb.match_id) >= 5 AND AVG(pb.overs_bowled) >= 2.0 
ORDER BY overall_economy ASC, total_wickets DESC;""",
        "chart_type": "bar",
        "x": "bowler_name",
        "y": "overall_economy"
    },
    19: {
        "title": "Batting Consistency & Standard Deviation",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Rank batsmen by stability and volatility using standard deviation of innings runs.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    COUNT(b.batting_id) AS innings_count, 
    ROUND(AVG(b.runs_scored), 2) AS avg_runs, 
    ROUND(SQRT(MAX(0, AVG(b.runs_scored * b.runs_scored) - AVG(b.runs_scored) * AVG(b.runs_scored))), 2) AS std_dev_runs 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
WHERE b.balls_faced >= 10 AND m.match_date >= '2022-01-01' 
GROUP BY p.player_id, p.full_name 
HAVING COUNT(b.batting_id) >= 3 
ORDER BY std_dev_runs ASC;""",
        "chart_type": "scatter",
        "x": "avg_runs",
        "y": "std_dev_runs"
    },
    20: {
        "title": "Multi-Format Match Distribution & Averages",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Analyze all-format workload distribution and respective batting averages.",
        "sql": """SELECT 
    p.full_name AS player_name, 
    COUNT(DISTINCT CASE WHEN m.match_format = 'Test' THEN m.match_id END) AS test_matches, 
    ROUND(AVG(CASE WHEN m.match_format = 'Test' THEN b.runs_scored END), 2) AS test_avg, 
    COUNT(DISTINCT CASE WHEN m.match_format = 'ODI' THEN m.match_id END) AS odi_matches, 
    ROUND(AVG(CASE WHEN m.match_format = 'ODI' THEN b.runs_scored END), 2) AS odi_avg, 
    COUNT(DISTINCT CASE WHEN m.match_format = 'T20I' THEN m.match_id END) AS t20i_matches, 
    ROUND(AVG(CASE WHEN m.match_format = 'T20I' THEN b.runs_scored END), 2) AS t20i_avg, 
    COUNT(DISTINCT m.match_id) AS total_matches 
FROM player_match_batting b 
JOIN players p ON b.player_id = p.player_id 
JOIN matches m ON b.match_id = m.match_id 
GROUP BY p.player_id, p.full_name 
HAVING total_matches >= 3 
ORDER BY total_matches DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "total_matches"
    },
    21: {
        "title": "Weighted Composite Player Ranking Formula",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Synthesize batting, bowling, and fielding into a unified algorithmic player valuation metric.",
        "sql": """WITH batting_stats AS (
    SELECT player_id, SUM(runs_scored) AS total_runs, AVG(runs_scored) AS batting_avg, AVG(strike_rate) AS avg_sr 
    FROM player_match_batting GROUP BY player_id
),
bowling_stats AS (
    SELECT player_id, SUM(wickets_taken) AS total_wickets, 
           AVG(CASE WHEN wickets_taken > 0 THEN runs_conceded * 1.0 / wickets_taken ELSE 35.0 END) AS bowling_avg, 
           AVG(economy_rate) AS avg_econ 
    FROM player_match_bowling GROUP BY player_id
),
fielding_stats AS (
    SELECT player_id, SUM(catches) AS total_catches, SUM(stumpings) AS total_stumpings 
    FROM player_match_fielding GROUP BY player_id
)
SELECT 
    p.full_name, 
    p.playing_role, 
    ROUND(COALESCE(b.total_runs * 0.01 + b.batting_avg * 0.5 + b.avg_sr * 0.3, 0), 2) AS batting_points, 
    ROUND(COALESCE(bw.total_wickets * 2 + (50 - bw.bowling_avg) * 0.5 + (6 - bw.avg_econ) * 2, 0), 2) AS bowling_points, 
    ROUND(COALESCE(f.total_catches * 3 + f.total_stumpings * 5, 0), 2) AS fielding_points, 
    ROUND(COALESCE(b.total_runs * 0.01 + b.batting_avg * 0.5 + b.avg_sr * 0.3, 0) + 
          COALESCE(bw.total_wickets * 2 + (50 - bw.bowling_avg) * 0.5 + (6 - bw.avg_econ) * 2, 0) + 
          COALESCE(f.total_catches * 3 + f.total_stumpings * 5, 0), 2) AS total_composite_score 
FROM players p 
LEFT JOIN batting_stats b ON p.player_id = b.player_id 
LEFT JOIN bowling_stats bw ON p.player_id = bw.player_id 
LEFT JOIN fielding_stats f ON p.player_id = f.player_id 
ORDER BY total_composite_score DESC;""",
        "chart_type": "bar",
        "x": "full_name",
        "y": "total_composite_score"
    },
    22: {
        "title": "Head-to-Head Match Prediction Analytics",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Predict competitive match edge and margin profiles between international rivals.",
        "sql": """SELECT 
    t1.team_name AS team_a, 
    t2.team_name AS team_b, 
    COUNT(m.match_id) AS total_matches, 
    SUM(CASE WHEN m.match_winner_id = t1.team_id THEN 1 ELSE 0 END) AS team_a_wins, 
    SUM(CASE WHEN m.match_winner_id = t2.team_id THEN 1 ELSE 0 END) AS team_b_wins, 
    ROUND(AVG(CASE WHEN m.match_winner_id = t1.team_id THEN m.win_margin END), 1) AS team_a_avg_margin, 
    ROUND(AVG(CASE WHEN m.match_winner_id = t2.team_id THEN m.win_margin END), 1) AS team_b_avg_margin, 
    ROUND(100.0 * SUM(CASE WHEN m.match_winner_id = t1.team_id THEN 1 ELSE 0 END) / COUNT(m.match_id), 1) AS team_a_win_pct, 
    ROUND(100.0 * SUM(CASE WHEN m.match_winner_id = t2.team_id THEN 1 ELSE 0 END) / COUNT(m.match_id), 1) AS team_b_win_pct 
FROM matches m 
JOIN teams t1 ON (m.team1_id = t1.team_id AND m.team2_id > t1.team_id) OR (m.team2_id = t1.team_id AND m.team1_id > t1.team_id) 
JOIN teams t2 ON (m.team1_id = t2.team_id AND t2.team_id > t1.team_id) OR (m.team2_id = t2.team_id AND t2.team_id > t1.team_id) 
GROUP BY team_a, team_b 
HAVING total_matches >= 3 
ORDER BY total_matches DESC;""",
        "chart_type": "table"
    },
    23: {
        "title": "Recent Player Form & Momentum Tracking",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Classify players into 'Excellent', 'Good', 'Average', or 'Poor' form using rolling last-5 vs last-10 performances.",
        "sql": """WITH ranked_innings AS (
    SELECT 
        b.player_id, 
        b.runs_scored, 
        b.strike_rate, 
        ROW_NUMBER() OVER (PARTITION BY b.player_id ORDER BY m.match_date DESC) AS rn 
    FROM player_match_batting b 
    JOIN matches m ON b.match_id = m.match_id
)
SELECT 
    p.full_name AS player_name, 
    ROUND(AVG(CASE WHEN r.rn <= 5 THEN r.runs_scored END), 2) AS last_5_avg_runs, 
    ROUND(AVG(CASE WHEN r.rn <= 10 THEN r.runs_scored END), 2) AS last_10_avg_runs, 
    ROUND(AVG(CASE WHEN r.rn <= 10 THEN r.strike_rate END), 2) AS recent_strike_rate, 
    SUM(CASE WHEN r.rn <= 10 AND r.runs_scored >= 50 THEN 1 ELSE 0 END) AS fifties_in_last_10, 
    CASE 
        WHEN AVG(CASE WHEN r.rn <= 5 THEN r.runs_scored END) >= 60 THEN 'Excellent Form' 
        WHEN AVG(CASE WHEN r.rn <= 5 THEN r.runs_scored END) >= 40 THEN 'Good Form' 
        WHEN AVG(CASE WHEN r.rn <= 5 THEN r.runs_scored END) >= 20 THEN 'Average Form' 
        ELSE 'Poor Form' 
    END AS form_category 
FROM ranked_innings r 
JOIN players p ON r.player_id = p.player_id 
WHERE r.rn <= 10 
GROUP BY p.player_id, p.full_name 
HAVING COUNT(r.rn) >= 3 
ORDER BY last_5_avg_runs DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "last_5_avg_runs"
    },
    24: {
        "title": "Batting Partnership Synergy & Success Rate",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Quantify batting combination chemistry, average partnership stands, and 50+ conversion rates.",
        "sql": """SELECT 
    p1.full_name AS batsman_1, 
    p2.full_name AS batsman_2, 
    COUNT(bp.partnership_id) AS total_partnerships, 
    ROUND(AVG(bp.partnership_runs), 2) AS avg_partnership_runs, 
    SUM(CASE WHEN bp.partnership_runs >= 50 THEN 1 ELSE 0 END) AS stands_above_50, 
    MAX(bp.partnership_runs) AS highest_partnership, 
    ROUND(100.0 * SUM(CASE WHEN bp.partnership_runs >= 50 THEN 1 ELSE 0 END) / COUNT(bp.partnership_id), 1) AS success_rate_pct 
FROM batting_partnerships bp 
JOIN players p1 ON bp.batsman1_id = p1.player_id 
JOIN players p2 ON bp.batsman2_id = p2.player_id 
GROUP BY p1.full_name, p2.full_name 
ORDER BY avg_partnership_runs DESC;""",
        "chart_type": "bar",
        "x": "batsman_1",
        "y": "avg_partnership_runs"
    },
    25: {
        "title": "Quarterly Time-Series Career Trajectory",
        "category": "Advanced",
        "level": "Hard",
        "business_problem": "Analyze player scoring momentum quarter-over-quarter and classify career phase: Ascending, Declining, or Stable.",
        "sql": """WITH quarterly_stats AS (
    SELECT 
        b.player_id, 
        strftime('%Y', m.match_date) || '-Q' || ((CAST(strftime('%m', m.match_date) AS INTEGER) + 2) / 3) AS quarter, 
        AVG(b.runs_scored) AS avg_runs, 
        AVG(b.strike_rate) AS avg_sr, 
        COUNT(b.batting_id) AS match_count 
    FROM player_match_batting b 
    JOIN matches m ON b.match_id = m.match_id 
    GROUP BY b.player_id, quarter
),
diff_stats AS (
    SELECT 
        q.*, 
        LAG(q.avg_runs) OVER (PARTITION BY q.player_id ORDER BY q.quarter) AS prev_quarter_runs 
    FROM quarterly_stats q
)
SELECT 
    p.full_name AS player_name, 
    COUNT(d.quarter) AS active_quarters, 
    ROUND(AVG(d.avg_runs), 2) AS career_quarterly_avg, 
    ROUND(COALESCE(AVG(d.avg_runs - d.prev_quarter_runs), 0), 2) AS avg_quarterly_momentum, 
    CASE 
        WHEN AVG(d.avg_runs - d.prev_quarter_runs) > 5.0 THEN 'Career Ascending' 
        WHEN AVG(d.avg_runs - d.prev_quarter_runs) < -5.0 THEN 'Career Declining' 
        ELSE 'Career Stable' 
    END AS career_phase 
FROM diff_stats d 
JOIN players p ON d.player_id = p.player_id 
GROUP BY p.player_id, p.full_name 
HAVING active_quarters >= 2 
ORDER BY avg_quarterly_momentum DESC;""",
        "chart_type": "bar",
        "x": "player_name",
        "y": "avg_quarterly_momentum"
    }
}
