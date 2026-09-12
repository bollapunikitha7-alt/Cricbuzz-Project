-- ==========================================================
-- INTERMEDIATE LEVEL SQL QUERIES (Questions 9 - 16)
-- ==========================================================

-- Q9: All-rounders who have scored runs and taken wickets across formats.
SELECT 
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
ORDER BY total_runs DESC;

-- Q10: Last 20 completed matches with victory margins.
SELECT 
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
LIMIT 20;

-- Q11: Compare player performance across formats (players with at least 2 formats).
SELECT 
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
ORDER BY overall_batting_avg DESC;

-- Q12: Home vs Away performance for each international team.
SELECT 
    t.team_name, 
    SUM(CASE WHEN v.country = t.country AND m.match_winner_id = t.team_id THEN 1 ELSE 0 END) AS home_wins, 
    SUM(CASE WHEN v.country != t.country AND m.match_winner_id = t.team_id THEN 1 ELSE 0 END) AS away_wins, 
    COUNT(CASE WHEN m.match_winner_id = t.team_id THEN 1 END) AS total_wins 
FROM teams t 
LEFT JOIN matches m ON t.team_id = m.team1_id OR t.team_id = m.team2_id 
LEFT JOIN venues v ON m.venue_id = v.venue_id 
GROUP BY t.team_id, t.team_name 
ORDER BY total_wins DESC;

-- Q13: Batting partnerships of 100+ runs by consecutive batsmen in same innings.
SELECT 
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
ORDER BY bp.partnership_runs DESC;

-- Q14: Bowling performance at different venues (>= 3 matches, >= 4 overs each).
SELECT 
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
ORDER BY total_wickets DESC, avg_economy ASC;

-- Q15: Clutch performers in close matches (< 50 runs or < 5 wickets).
SELECT 
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
ORDER BY avg_runs DESC;

-- Q16: Batting performance evolution by year (2020+).
SELECT 
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
ORDER BY p.full_name, match_year ASC;
