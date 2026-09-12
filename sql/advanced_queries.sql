-- ==========================================================
-- ADVANCED LEVEL SQL QUERIES (Questions 17 - 25)
-- ==========================================================

-- Q17: Toss win advantage percentage segmented by bat/bowl decision.
SELECT 
    toss_decision, 
    COUNT(*) AS total_matches, 
    SUM(CASE WHEN toss_winner_id = match_winner_id THEN 1 ELSE 0 END) AS matches_won, 
    ROUND(100.0 * SUM(CASE WHEN toss_winner_id = match_winner_id THEN 1 ELSE 0 END) / COUNT(*), 2) AS win_percentage 
FROM matches 
WHERE match_winner_id IS NOT NULL 
GROUP BY toss_decision;

-- Q18: Most economical bowlers in limited-overs cricket (ODI & T20I).
SELECT 
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
ORDER BY overall_economy ASC, total_wickets DESC;

-- Q19: Batsman consistency: average runs & standard deviation (>= 10 balls faced, 2022+).
SELECT 
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
ORDER BY std_dev_runs ASC;

-- Q20: Format distribution and batting average per format.
SELECT 
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
ORDER BY total_matches DESC;

-- Q21: Comprehensive weighted composite performance ranking.
WITH batting_stats AS (
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
ORDER BY total_composite_score DESC;

-- Q22: Head-to-head match prediction analysis between teams.
SELECT 
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
ORDER BY total_matches DESC;

-- Q23: Form & momentum tracking: Last 5 vs last 10 matches.
WITH ranked_innings AS (
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
ORDER BY last_5_avg_runs DESC;

-- Q24: Consecutive batsmen partnership synergy.
SELECT 
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
ORDER BY avg_partnership_runs DESC;

-- Q25: Quarterly time-series career phase analysis.
WITH quarterly_stats AS (
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
ORDER BY avg_quarterly_momentum DESC;
