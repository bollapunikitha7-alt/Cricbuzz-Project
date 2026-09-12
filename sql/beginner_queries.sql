-- ==========================================================
-- BEGINNER LEVEL SQL QUERIES (Questions 1 - 8)
-- ==========================================================

-- Q1: Find all players who represent India. Display full name, role, batting style, and bowling style.
SELECT 
    p.full_name, 
    p.playing_role, 
    p.batting_style, 
    p.bowling_style 
FROM players p 
JOIN teams t ON p.team_id = t.team_id 
WHERE t.team_name = 'India' 
ORDER BY p.full_name ASC;

-- Q2: Show all matches in the last 30 days (or most recent relative window) sorted chronologically.
SELECT 
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
ORDER BY m.match_date DESC;

-- Q3: Top 10 highest run scorers in ODI cricket with average and centuries.
SELECT 
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
LIMIT 10;

-- Q4: Venues with seating capacity > 50,000 spectators ordered by largest capacity.
SELECT 
    venue_name, 
    city, 
    country, 
    capacity 
FROM venues 
WHERE capacity > 50000 
ORDER BY capacity DESC;

-- Q5: Match win counts per team.
SELECT 
    t.team_name, 
    COUNT(m.match_id) AS total_wins 
FROM teams t 
JOIN matches m ON t.team_id = m.match_winner_id 
GROUP BY t.team_id, t.team_name 
ORDER BY total_wins DESC;

-- Q6: Count players belonging to each playing role.
SELECT 
    playing_role, 
    COUNT(player_id) AS player_count 
FROM players 
GROUP BY playing_role 
ORDER BY player_count DESC;

-- Q7: Highest individual batting score achieved in each cricket format.
SELECT 
    m.match_format, 
    MAX(b.runs_scored) AS highest_score 
FROM player_match_batting b 
JOIN matches m ON b.match_id = m.match_id 
GROUP BY m.match_format 
ORDER BY highest_score DESC;

-- Q8: Series that started in 2024.
SELECT 
    series_name, 
    host_country, 
    match_type, 
    start_date, 
    total_matches 
FROM series 
WHERE strftime('%Y', start_date) = '2024' 
ORDER BY start_date ASC;
