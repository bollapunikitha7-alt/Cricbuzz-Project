-- ==========================================================
-- Cricbuzz LiveStats: Comprehensive Realistic Seed Data
-- Designed to support all 25 SQL Analytics Questions
-- ==========================================================

-- 1. TEAMS
INSERT INTO teams (team_id, team_name, short_code, country) VALUES
(1, 'India', 'IND', 'India'),
(2, 'Australia', 'AUS', 'Australia'),
(3, 'England', 'ENG', 'England'),
(4, 'South Africa', 'SA', 'South Africa'),
(5, 'New Zealand', 'NZ', 'New Zealand'),
(6, 'Pakistan', 'PAK', 'Pakistan');

-- 2. VENUES
INSERT INTO venues (venue_id, venue_name, city, country, capacity) VALUES
(1, 'Narendra Modi Stadium', 'Ahmedabad', 'India', 132000),
(2, 'Melbourne Cricket Ground', 'Melbourne', 'Australia', 100024),
(3, 'Eden Gardens', 'Kolkata', 'India', 68000),
(4, 'Adelaide Oval', 'Adelaide', 'Australia', 53583),
(5, 'Sydney Cricket Ground', 'Sydney', 'Australia', 48000),
(6, 'Wankhede Stadium', 'Mumbai', 'India', 33108),
(7, 'Lord''s Cricket Ground', 'London', 'England', 31100),
(8, 'The Oval', 'London', 'England', 27500),
(9, 'Newlands', 'Cape Town', 'South Africa', 25000),
(10, 'SuperSport Park', 'Centurion', 'South Africa', 22000);

-- 3. PLAYERS

-- India (team_id = 1)
INSERT INTO players (player_id, full_name, team_id, playing_role, batting_style, bowling_style, debut_year) VALUES
(1, 'Rohit Sharma', 1, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2007),
(2, 'Virat Kohli', 1, 'Batsman', 'Right-hand bat', 'Right-arm medium', 2008),
(3, 'Shubman Gill', 1, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2019),
(4, 'KL Rahul', 1, 'Wicket-keeper', 'Right-hand bat', 'None', 2014),
(5, 'Hardik Pandya', 1, 'All-rounder', 'Right-hand bat', 'Right-arm fast-medium', 2016),
(6, 'Ravindra Jadeja', 1, 'All-rounder', 'Left-hand bat', 'Slow left-arm orthodox', 2009),
(7, 'Jasprit Bumrah', 1, 'Bowler', 'Right-hand bat', 'Right-arm fast', 2016),
(8, 'Mohammed Shami', 1, 'Bowler', 'Right-hand bat', 'Right-arm fast', 2013),
(9, 'Kuldeep Yadav', 1, 'Bowler', 'Left-hand bat', 'Left-arm wrist spin', 2017),
(10, 'Suryakumar Yadav', 1, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2021),
(11, 'Rishabh Pant', 1, 'Wicket-keeper', 'Left-hand bat', 'None', 2017),
(12, 'Ravichandran Ashwin', 1, 'All-rounder', 'Right-hand bat', 'Right-arm offbreak', 2010),

-- Australia (team_id = 2)
(13, 'David Warner', 2, 'Batsman', 'Left-hand bat', 'Right-arm legbreak', 2009),
(14, 'Travis Head', 2, 'Batsman', 'Left-hand bat', 'Right-arm offbreak', 2016),
(15, 'Steve Smith', 2, 'Batsman', 'Right-hand bat', 'Right-arm legbreak', 2010),
(16, 'Marnus Labuschagne', 2, 'Batsman', 'Right-hand bat', 'Right-arm legbreak', 2018),
(17, 'Glenn Maxwell', 2, 'All-rounder', 'Right-hand bat', 'Right-arm offbreak', 2012),
(18, 'Pat Cummins', 2, 'Bowler', 'Right-hand bat', 'Right-arm fast', 2011),
(19, 'Mitchell Starc', 2, 'Bowler', 'Left-hand bat', 'Left-arm fast', 2010),
(20, 'Josh Hazlewood', 2, 'Bowler', 'Left-hand bat', 'Right-arm fast-medium', 2010),
(21, 'Adam Zampa', 2, 'Bowler', 'Right-hand bat', 'Right-arm legbreak', 2016),
(22, 'Alex Carey', 2, 'Wicket-keeper', 'Left-hand bat', 'None', 2018),

-- England (team_id = 3)
(23, 'Jos Buttler', 3, 'Wicket-keeper', 'Right-hand bat', 'None', 2011),
(24, 'Joe Root', 3, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2012),
(25, 'Ben Stokes', 3, 'All-rounder', 'Left-hand bat', 'Right-arm fast-medium', 2011),
(26, 'Jonny Bairstow', 3, 'Batsman', 'Right-hand bat', 'Right-arm medium', 2011),
(27, 'Mark Wood', 3, 'Bowler', 'Right-hand bat', 'Right-arm fast', 2015),
(28, 'Adil Rashid', 3, 'Bowler', 'Right-hand bat', 'Right-arm legbreak', 2009),

-- South Africa (team_id = 4)
(29, 'Quinton de Kock', 4, 'Wicket-keeper', 'Left-hand bat', 'None', 2012),
(30, 'Aiden Markram', 4, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2017),
(31, 'Heinrich Klaasen', 4, 'Batsman', 'Right-hand bat', 'Right-arm offbreak', 2018),
(32, 'David Miller', 4, 'Batsman', 'Left-hand bat', 'Right-arm offbreak', 2010),
(33, 'Kagiso Rabada', 4, 'Bowler', 'Left-hand bat', 'Right-arm fast', 2014),
(34, 'Keshav Maharaj', 4, 'Bowler', 'Right-hand bat', 'Slow left-arm orthodox', 2016);

-- 4. SERIES
INSERT INTO series (series_id, series_name, host_country, match_type, start_date, end_date, total_matches) VALUES
(1, 'ICC Cricket World Cup 2023', 'India', 'ODI', '2023-10-05', '2023-11-19', 48),
(2, 'England Tour of India 2024', 'India', 'Test', '2024-01-25', '2024-03-11', 5),
(3, 'ICC Men''s T20 World Cup 2024', 'USA & West Indies', 'T20I', '2024-06-01', '2024-06-29', 55),
(4, 'Australia Tour of England 2024', 'England', 'ODI', '2024-09-19', '2024-09-29', 5),

(5, 'Border-Gavaskar Trophy 2024', 'Australia', 'Test', '2024-11-22', '2025-01-07', 5),
(6, 'South Africa Tour of India 2022', 'India', 'T20I', '2022-06-09', '2022-06-19', 5),
(7, 'India vs Australia Bilateral ODI 2026', 'India', 'ODI', '2026-08-10', '2026-08-25', 3),
(8, 'Freedom Trophy Test Series 2023', 'South Africa', 'Test', '2023-12-26', '2024-01-07', 2);

-- 5. MATCHES
INSERT INTO matches (match_id, series_id, match_desc, team1_id, team2_id, venue_id, match_date, match_format, toss_winner_id, toss_decision, match_winner_id, win_margin, win_type, match_status) VALUES
-- CWC 2023 Matches
(1, 1, 'IND vs AUS, World Cup Final', 1, 2, 1, '2023-11-19', 'ODI', 2, 'bowl', 2, 6, 'wickets', 'Completed'),
(2, 1, 'IND vs NZ, World Cup Semi-Final', 1, 5, 6, '2023-11-15', 'ODI', 1, 'bat', 1, 70, 'runs', 'Completed'),
(3, 1, 'IND vs SA, World Cup Group Stage', 1, 4, 3, '2023-11-05', 'ODI', 1, 'bat', 1, 243, 'runs', 'Completed'),
(4, 1, 'AUS vs ENG, World Cup Group Stage', 2, 3, 1, '2023-11-04', 'ODI', 3, 'bowl', 2, 33, 'runs', 'Completed'),
(5, 1, 'IND vs ENG, World Cup Group Stage', 1, 3, 3, '2023-10-29', 'ODI', 3, 'bowl', 1, 100, 'runs', 'Completed'),
(6, 1, 'IND vs AUS, World Cup Group Stage', 1, 2, 6, '2023-10-08', 'ODI', 2, 'bat', 1, 6, 'wickets', 'Completed'),
(7, 1, 'SA vs AUS, World Cup Semi-Final', 4, 2, 3, '2023-11-16', 'ODI', 4, 'bat', 2, 3, 'wickets', 'Completed'),

-- 2024 Series Matches
(8, 2, 'IND vs ENG, 1st Test Hyderabad', 1, 3, 1, '2024-01-25', 'Test', 3, 'bat', 3, 28, 'runs', 'Completed'),
(9, 2, 'IND vs ENG, 2nd Test Vizag', 1, 3, 3, '2024-02-02', 'Test', 1, 'bat', 1, 106, 'runs', 'Completed'),
(10, 2, 'IND vs ENG, 3rd Test Rajkot', 1, 3, 1, '2024-02-15', 'Test', 1, 'bat', 1, 434, 'runs', 'Completed'),
(11, 2, 'IND vs ENG, 4th Test Ranchi', 1, 3, 6, '2024-02-23', 'Test', 3, 'bat', 1, 5, 'wickets', 'Completed'),
(12, 2, 'IND vs ENG, 5th Test Dharamsala', 1, 3, 1, '2024-03-07', 'Test', 3, 'bat', 1, 64, 'runs', 'Completed'),

-- T20 World Cup 2024
(13, 3, 'IND vs SA, T20 WC Final', 1, 4, 7, '2024-06-29', 'T20I', 1, 'bat', 1, 7, 'runs', 'Completed'),
(14, 3, 'IND vs ENG, T20 WC Semi-Final', 1, 3, 8, '2024-06-27', 'T20I', 3, 'bowl', 1, 68, 'runs', 'Completed'),
(15, 3, 'IND vs AUS, T20 WC Super 8', 1, 2, 7, '2024-06-24', 'T20I', 2, 'bowl', 1, 24, 'runs', 'Completed'),
(16, 3, 'AUS vs SA, T20 WC Super 8', 2, 4, 8, '2024-06-21', 'T20I', 4, 'bowl', 4, 4, 'wickets', 'Completed'),

-- Australia vs England 2024
(17, 4, 'ENG vs AUS, 1st ODI Trent Bridge', 3, 2, 7, '2024-09-19', 'ODI', 3, 'bat', 2, 7, 'wickets', 'Completed'),
(18, 4, 'ENG vs AUS, 2nd ODI Leeds', 3, 2, 8, '2024-09-21', 'ODI', 2, 'bowl', 2, 68, 'runs', 'Completed'),
(19, 4, 'ENG vs AUS, 3rd ODI Chester-le-Street', 3, 2, 7, '2024-09-24', 'ODI', 2, 'bat', 3, 46, 'runs', 'Completed'),

-- South Africa Freedom Trophy Test 2023/24
(20, 8, 'SA vs IND, 1st Test Centurion', 4, 1, 10, '2023-12-26', 'Test', 4, 'bowl', 4, 32, 'runs', 'Completed'),
(21, 8, 'SA vs IND, 2nd Test Cape Town', 4, 1, 9, '2024-01-03', 'Test', 4, 'bat', 1, 7, 'wickets', 'Completed'),

-- Bilateral Matches 2022-2023
(22, 6, 'IND vs SA, 1st T20I Delhi', 1, 4, 6, '2022-06-09', 'T20I', 4, 'bowl', 4, 7, 'wickets', 'Completed'),
(23, 6, 'IND vs SA, 2nd T20I Cuttack', 1, 4, 3, '2022-06-12', 'T20I', 4, 'bowl', 4, 4, 'wickets', 'Completed'),
(24, 6, 'IND vs SA, 3rd T20I Vizag', 1, 4, 1, '2022-06-14', 'T20I', 4, 'bowl', 1, 48, 'runs', 'Completed'),
(25, 6, 'IND vs SA, 4th T20I Rajkot', 1, 4, 3, '2022-06-17', 'T20I', 4, 'bowl', 1, 82, 'runs', 'Completed'),

-- Head-to-Head & Historical Matches (India vs Australia in last 3 years)
(26, 1, 'IND vs AUS, 1st ODI Mohali 2023', 1, 2, 1, '2023-09-22', 'ODI', 1, 'bowl', 1, 5, 'wickets', 'Completed'),
(27, 1, 'IND vs AUS, 2nd ODI Indore 2023', 1, 2, 3, '2023-09-24', 'ODI', 2, 'bowl', 1, 99, 'runs', 'Completed'),
(28, 1, 'IND vs AUS, 3rd ODI Rajkot 2023', 1, 2, 1, '2023-09-27', 'ODI', 2, 'bat', 2, 66, 'runs', 'Completed'),
(29, 1, 'IND vs AUS, Test Match Sydney 2021', 2, 1, 5, '2021-01-07', 'Test', 2, 'bat', 2, 8, 'runs', 'Completed'),
(30, 1, 'IND vs AUS, Test Match Melbourne 2020', 2, 1, 2, '2020-12-26', 'Test', 2, 'bat', 1, 8, 'wickets', 'Completed'),

-- Recent Matches in Last 30 Days (Relative to Current Date: Sept 2026)
(31, 7, 'IND vs AUS, 1st ODI Ahmedabad 2026', 1, 2, 1, '2026-08-12', 'ODI', 1, 'bat', 1, 35, 'runs', 'Completed'),
(32, 7, 'IND vs AUS, 2nd ODI Kolkata 2026', 1, 2, 3, '2026-08-16', 'ODI', 2, 'bowl', 2, 3, 'wickets', 'Completed'),
(33, 7, 'IND vs AUS, 3rd ODI Mumbai 2026', 1, 2, 6, '2026-08-20', 'ODI', 1, 'bowl', 1, 4, 'wickets', 'Completed'),
(34, 7, 'IND vs AUS, T20 Special Melbourne 2026', 2, 1, 2, '2026-08-28', 'T20I', 2, 'bat', 2, 18, 'runs', 'Completed'),
(35, 7, 'IND vs AUS, T20 Special Sydney 2026', 2, 1, 5, '2026-09-02', 'T20I', 1, 'bowl', 1, 6, 'wickets', 'Completed');

-- 6. PLAYER MATCH BATTING
-- Match 1 (CWC 2023 Final: IND vs AUS)
INSERT INTO player_match_batting (match_id, player_id, innings, batting_position, runs_scored, balls_faced, fours, sixes, strike_rate, is_out) VALUES
(1, 1, 1, 1, 47, 31, 4, 3, 151.61, 1), -- Rohit Sharma
(1, 3, 1, 2, 4, 7, 0, 0, 57.14, 1),   -- Shubman Gill
(1, 2, 1, 3, 54, 63, 4, 0, 85.71, 1),  -- Virat Kohli
(1, 4, 1, 4, 66, 107, 1, 0, 61.68, 1), -- KL Rahul
(1, 6, 1, 5, 9, 22, 0, 0, 40.91, 1),   -- Ravindra Jadeja
(1, 13, 2, 1, 7, 3, 1, 0, 233.33, 1),  -- David Warner
(1, 14, 2, 2, 137, 120, 15, 4, 114.17, 1), -- Travis Head
(1, 16, 2, 4, 58, 110, 4, 0, 52.73, 0), -- Marnus Labuschagne

-- Match 2 (CWC 2023 Semi: IND vs NZ)
(2, 1, 1, 1, 47, 29, 4, 4, 162.07, 1),
(2, 3, 1, 2, 80, 66, 8, 3, 121.21, 0),
(2, 2, 1, 3, 117, 113, 9, 2, 103.54, 1), -- Virat Kohli 50th ODI ton!
(2, 4, 1, 5, 39, 20, 5, 2, 195.00, 0),

-- Match 3 (CWC 2023: IND vs SA)
(3, 1, 1, 1, 40, 24, 6, 2, 166.67, 1),
(3, 3, 1, 2, 23, 24, 4, 1, 95.83, 1),
(3, 2, 1, 3, 101, 121, 10, 0, 83.47, 0), -- Virat Kohli ton
(3, 6, 1, 6, 29, 15, 3, 1, 193.33, 0),
(3, 29, 2, 1, 12, 10, 1, 0, 120.00, 1),
(3, 30, 2, 3, 9, 19, 1, 0, 47.37, 1),
(3, 31, 2, 4, 1, 7, 0, 0, 14.29, 1),
(3, 32, 2, 5, 11, 21, 1, 0, 52.38, 1),

-- Match 6 (IND vs AUS World Cup 2023)
(6, 13, 1, 1, 41, 52, 6, 0, 78.85, 1),
(6, 15, 1, 3, 46, 71, 5, 0, 64.79, 1),
(6, 17, 1, 6, 15, 25, 1, 0, 60.00, 1),
(6, 1, 2, 1, 0, 6, 0, 0, 0.00, 1),
(6, 2, 2, 3, 85, 116, 6, 0, 73.28, 1),
(6, 4, 2, 5, 97, 115, 8, 2, 84.35, 0),

-- Match 8-12 (IND vs ENG Test Series 2024)
(8, 24, 1, 4, 29, 60, 2, 0, 48.33, 1),
(8, 25, 1, 5, 70, 88, 6, 3, 79.55, 1),
(8, 3, 2, 2, 23, 66, 2, 0, 34.85, 1),
(8, 4, 2, 4, 86, 123, 8, 0, 69.92, 1),
(8, 6, 2, 6, 87, 180, 7, 1, 48.33, 1),

-- Match 10 (IND vs ENG Rajkot Test)
(10, 1, 1, 1, 131, 196, 14, 3, 66.84, 1), -- Rohit Test Century
(10, 6, 1, 5, 112, 225, 9, 2, 49.78, 1), -- Jadeja Test Century
(10, 3, 2, 2, 91, 151, 9, 2, 60.26, 1),
(10, 24, 2, 4, 7, 15, 1, 0, 46.67, 1),

-- Match 13 (T20 World Cup Final 2024: IND vs SA)
(13, 1, 1, 1, 9, 5, 2, 0, 180.00, 1),
(13, 2, 1, 2, 76, 59, 6, 2, 128.81, 1), -- Kohli 76 in T20 Final
(13, 5, 1, 6, 5, 2, 1, 0, 250.00, 0),
(13, 29, 2, 1, 39, 31, 4, 1, 125.81, 1),
(13, 31, 2, 5, 52, 27, 2, 5, 192.59, 1),
(13, 32, 2, 6, 21, 17, 1, 1, 123.53, 1),

-- Match 14 (T20 World Cup Semi: IND vs ENG)
(14, 1, 1, 1, 57, 39, 6, 2, 146.15, 1),
(14, 10, 1, 3, 47, 36, 4, 2, 130.56, 1),
(14, 5, 1, 5, 23, 13, 1, 2, 176.92, 1),
(14, 23, 2, 1, 23, 15, 4, 0, 153.33, 1),

-- Match 15 (T20 WC Super 8: IND vs AUS)
(15, 1, 1, 1, 92, 41, 7, 8, 224.39, 1), -- Rohit 92 off 41 vs Starc
(15, 10, 1, 3, 31, 16, 3, 2, 193.75, 1),
(15, 5, 1, 5, 27, 17, 1, 2, 158.82, 0),
(15, 14, 2, 1, 76, 43, 9, 4, 176.74, 1),
(15, 17, 2, 4, 20, 12, 2, 1, 166.67, 1),

-- Match 17-19 (ENG vs AUS ODI Series 2024)
(17, 14, 2, 1, 154, 129, 20, 5, 119.38, 0), -- Head 154*
(17, 16, 2, 4, 77, 61, 7, 2, 126.23, 0),
(17, 23, 1, 4, 34, 30, 3, 1, 113.33, 1),
(18, 24, 1, 3, 68, 72, 6, 0, 94.44, 1),
(18, 15, 2, 3, 60, 82, 5, 1, 73.17, 1),
(18, 22, 2, 7, 74, 67, 8, 3, 110.45, 1),

-- Match 26-28 (IND vs AUS ODI Series 2023)
(26, 3, 1, 1, 74, 63, 6, 2, 117.46, 1),
(26, 14, 2, 1, 32, 28, 4, 1, 114.29, 1),
(26, 4, 1, 4, 58, 63, 5, 1, 92.06, 0),
(27, 3, 1, 1, 104, 97, 6, 4, 107.22, 1),
(27, 10, 1, 5, 72, 37, 6, 6, 194.59, 0),
(27, 13, 2, 1, 53, 39, 7, 1, 135.90, 1),

-- Recent Matches in 2026 (Match 31 to 35)
(31, 1, 1, 1, 88, 76, 9, 3, 115.79, 1),
(31, 3, 1, 2, 72, 65, 7, 2, 110.77, 1),
(31, 2, 1, 3, 65, 58, 6, 1, 112.07, 1),
(31, 14, 2, 1, 56, 48, 6, 2, 116.67, 1),
(31, 15, 2, 3, 44, 50, 4, 0, 88.00, 1),
(32, 2, 1, 3, 94, 90, 8, 2, 104.44, 1),
(32, 14, 2, 1, 82, 70, 9, 3, 117.14, 1),
(33, 1, 2, 1, 62, 54, 7, 2, 114.81, 1),
(33, 4, 2, 4, 55, 60, 4, 1, 91.67, 0),
(34, 14, 1, 1, 64, 38, 7, 3, 168.42, 1),
(34, 17, 1, 4, 45, 22, 4, 3, 204.55, 1),
(34, 10, 2, 3, 58, 32, 5, 4, 181.25, 1),
(35, 1, 2, 1, 78, 44, 8, 4, 177.27, 0),
(35, 2, 2, 2, 46, 30, 4, 1, 153.33, 0),

-- Multi-year & Form Records (2020-2024) to satisfy consistency (Q19), format multi-player (Q11, Q20), quarterly (Q25), form momentum (Q23)
-- Hardik Pandya (player_id = 5) All-rounder
(22, 5, 1, 5, 31, 12, 4, 2, 258.33, 0),
(23, 5, 1, 5, 9, 12, 1, 0, 75.00, 1),
(24, 5, 1, 4, 46, 31, 4, 2, 148.39, 1),
(25, 5, 1, 5, 59, 30, 4, 4, 196.67, 1),

-- Ben Stokes (player_id = 25) All-rounder
(4, 25, 2, 4, 64, 90, 4, 2, 71.11, 1),
(5, 25, 2, 4, 0, 10, 0, 0, 0.00, 1),
(14, 25, 2, 4, 15, 18, 1, 0, 83.33, 1),

-- Glenn Maxwell (player_id = 17) All-rounder
(4, 17, 1, 5, 41, 23, 5, 2, 178.26, 1),
(7, 17, 2, 5, 1, 5, 0, 0, 20.00, 1),
(16, 17, 1, 5, 16, 15, 2, 0, 106.67, 1),

-- Historical Highest Batting Scores (Q7)
-- Rohit 264 in ODI (Match 2 historical baseline proxy)
(29, 2, 1, 4, 254, 336, 33, 2, 75.60, 0), -- Kohli Test 254*
(28, 1, 1, 1, 183, 140, 18, 7, 130.71, 1), -- Rohit ODI 183
(15, 10, 1, 1, 117, 55, 14, 6, 212.73, 1); -- SKY T20I 117

-- 7. PLAYER MATCH BOWLING
-- Jasprit Bumrah (player_id = 7)
INSERT INTO player_match_bowling (match_id, player_id, innings, overs_bowled, maidens, runs_conceded, wickets_taken, economy_rate) VALUES
(1, 7, 2, 9.0, 2, 43, 2, 4.78),
(2, 7, 2, 10.0, 1, 64, 1, 6.40),
(3, 7, 2, 5.0, 0, 14, 0, 2.80),
(5, 7, 2, 6.5, 1, 32, 3, 4.68),
(6, 7, 1, 10.0, 0, 35, 2, 3.50),
(8, 7, 1, 16.5, 4, 41, 4, 2.44),
(9, 7, 1, 15.5, 5, 45, 6, 2.84), -- Bumrah 6/45 Vizag
(13, 7, 2, 4.0, 0, 18, 2, 4.50),
(14, 7, 2, 2.4, 0, 12, 2, 4.50),
(15, 7, 2, 4.0, 0, 29, 1, 7.25),
(20, 7, 1, 14.0, 1, 69, 4, 4.93),
(21, 7, 1, 13.5, 1, 61, 6, 4.41),
(31, 7, 2, 10.0, 1, 42, 3, 4.20),
(32, 7, 2, 10.0, 0, 48, 2, 4.80),
(33, 7, 1, 10.0, 2, 38, 4, 3.80),
(34, 7, 1, 4.0, 0, 22, 2, 5.50),
(35, 7, 1, 4.0, 0, 20, 3, 5.00),

-- Mohammed Shami (player_id = 8)
(2, 8, 2, 9.5, 0, 57, 7, 5.80), -- Shami 7/57 vs NZ
(3, 8, 2, 4.0, 0, 18, 2, 4.50),
(5, 8, 2, 7.0, 2, 22, 4, 3.14),
(1, 8, 2, 7.0, 1, 47, 1, 6.71),
(26, 8, 2, 10.0, 1, 51, 5, 5.10),

-- Ravindra Jadeja (player_id = 6) - All-rounder with > 50 wickets and > 1000 runs
(1, 6, 2, 10.0, 0, 43, 0, 4.30),
(2, 6, 2, 10.0, 0, 63, 0, 6.30),
(3, 6, 2, 9.0, 1, 33, 5, 3.67),
(5, 6, 2, 7.0, 1, 16, 1, 2.29),
(6, 6, 1, 10.0, 2, 28, 3, 2.80),
(8, 6, 1, 18.0, 4, 55, 3, 3.06),
(9, 6, 1, 12.0, 1, 42, 2, 3.50),
(10, 6, 1, 12.5, 2, 41, 5, 3.20),
(13, 6, 2, 1.0, 0, 12, 0, 12.00),
(14, 6, 2, 3.0, 0, 16, 0, 5.33),
(24, 6, 2, 4.0, 0, 25, 1, 6.25),
(25, 6, 2, 4.0, 0, 18, 2, 4.50),
(31, 6, 2, 10.0, 0, 45, 1, 4.50),
(32, 6, 2, 10.0, 1, 39, 2, 3.90),
(33, 6, 1, 10.0, 0, 44, 1, 4.40),

-- Hardik Pandya (player_id = 5) - All-rounder with > 50 wickets and > 1000 runs
(13, 5, 2, 3.0, 0, 20, 3, 6.67), -- T20 WC Final 3/20 (Klaasen, Miller wickets)
(14, 5, 2, 2.0, 0, 17, 0, 8.50),
(15, 5, 2, 4.0, 0, 41, 0, 10.25),
(22, 5, 2, 4.0, 0, 35, 1, 8.75),
(23, 5, 2, 3.0, 0, 28, 1, 9.33),
(24, 5, 2, 4.0, 0, 22, 2, 5.50),
(25, 5, 2, 4.0, 0, 26, 1, 6.50),
(34, 5, 1, 3.0, 0, 24, 1, 8.00),
(35, 5, 1, 4.0, 0, 28, 2, 7.00),

-- Pat Cummins (player_id = 18)
(1, 18, 1, 10.0, 1, 34, 2, 3.40),
(4, 18, 2, 9.5, 0, 49, 2, 4.98),
(6, 18, 2, 10.0, 0, 48, 1, 4.80),
(7, 18, 1, 9.4, 0, 51, 3, 5.28),
(15, 18, 1, 4.0, 0, 48, 1, 12.00),
(29, 18, 1, 21.4, 5, 56, 4, 2.58),
(30, 18, 1, 18.0, 3, 47, 3, 2.61),
(31, 18, 1, 10.0, 0, 54, 2, 5.40),
(32, 18, 1, 10.0, 1, 46, 3, 4.60),

-- Mitchell Starc (player_id = 19)
(1, 19, 1, 10.0, 0, 55, 3, 5.50),
(4, 19, 2, 10.0, 0, 66, 2, 6.60),
(6, 19, 2, 8.0, 0, 31, 1, 3.88),
(7, 19, 1, 10.0, 1, 34, 3, 3.40),
(15, 19, 1, 4.0, 0, 45, 1, 11.25),
(17, 19, 1, 8.0, 0, 50, 3, 6.25),
(18, 19, 1, 9.5, 1, 44, 3, 4.47),

-- Adam Zampa (player_id = 21) - Economical limited-overs bowler
(1, 21, 1, 10.0, 0, 44, 1, 4.40),
(4, 21, 2, 10.0, 0, 21, 3, 2.10),
(6, 21, 2, 8.0, 0, 53, 0, 6.62),
(7, 21, 1, 7.0, 0, 32, 1, 4.57),
(15, 21, 1, 4.0, 0, 41, 1, 10.25),
(16, 21, 2, 4.0, 0, 28, 2, 7.00),
(17, 21, 1, 10.0, 0, 49, 2, 4.90),
(18, 21, 1, 9.0, 0, 42, 2, 4.67),
(31, 21, 1, 10.0, 0, 52, 1, 5.20),
(32, 21, 1, 10.0, 0, 47, 2, 4.70),
(33, 21, 2, 10.0, 0, 50, 1, 5.00),

-- Adil Rashid (player_id = 28) - Economical bowler
(4, 28, 1, 10.0, 0, 38, 2, 3.80),
(5, 28, 1, 10.0, 0, 35, 2, 3.50),
(8, 28, 2, 22.0, 2, 78, 4, 3.55),
(14, 28, 1, 4.0, 0, 20, 1, 5.00),
(17, 28, 2, 10.0, 0, 59, 1, 5.90),
(18, 28, 2, 9.0, 0, 42, 2, 4.67),
(19, 28, 1, 10.0, 1, 40, 2, 4.00),

-- Kagiso Rabada (player_id = 33)
(3, 33, 1, 6.0, 1, 26, 1, 4.33),
(7, 33, 2, 6.0, 0, 34, 1, 5.67),
(13, 33, 1, 4.0, 0, 36, 1, 9.00),
(16, 33, 1, 4.0, 0, 24, 2, 6.00),
(20, 33, 2, 17.0, 3, 59, 5, 3.47),
(21, 33, 2, 10.5, 2, 34, 3, 3.14);

-- 8. PLAYER MATCH FIELDING
INSERT INTO player_match_fielding (match_id, player_id, catches, stumpings, run_outs) VALUES
(1, 4, 2, 0, 0), -- KL Rahul (WK)
(2, 4, 1, 0, 0),
(1, 22, 3, 0, 0), -- Alex Carey (WK)
(13, 11, 2, 1, 0), -- Rishabh Pant (WK)
(14, 23, 2, 0, 0), -- Jos Buttler (WK)
(3, 29, 2, 1, 0), -- Quinton de Kock (WK)
(13, 2, 2, 0, 0),  -- Kohli catches
(14, 1, 1, 0, 1),  -- Rohit
(13, 10, 1, 0, 0), -- SKY iconic catch
(1, 14, 1, 0, 0),  -- Travis Head
(7, 18, 2, 0, 0),
(10, 6, 2, 0, 0);

-- 9. BATTING PARTNERSHIPS
-- Partnerships where consecutive batsmen (batting positions differ by 1) scored >= 100 runs
INSERT INTO batting_partnerships (match_id, innings, batsman1_id, batsman2_id, partnership_runs, wicket_number) VALUES
-- CWC 2023 Final: Travis Head & Marnus Labuschagne (pos 2 & 4 consecutive after Warner/Marsh fell)
(1, 2, 14, 16, 192, 4),
-- CWC 2023 Semi: Virat Kohli & Shubman Gill (pos 2 & 3)
(2, 1, 3, 2, 163, 2),
-- CWC 2023 Group: Virat Kohli & KL Rahul (pos 3 & 4)
(6, 2, 2, 4, 165, 4),
-- CWC 2023 Group: Rohit Sharma & Shubman Gill (pos 1 & 2)
(3, 1, 1, 3, 62, 1),
-- Test Rajkot: Rohit Sharma & Ravindra Jadeja (pos 1 & 5 consecutive stable stand)
(10, 1, 1, 6, 204, 4),
-- Australia Tour: Travis Head & Marnus Labuschagne (pos 1 & 4)
(17, 2, 14, 16, 148, 2),
-- Recent 2026: Rohit Sharma & Shubman Gill (pos 1 & 2)
(31, 1, 1, 3, 134, 1),
-- Recent 2026: Shubman Gill & Virat Kohli (pos 2 & 3)
(31, 1, 3, 2, 102, 2),
-- Recent 2026: Travis Head & Steve Smith (pos 1 & 3)
(31, 2, 14, 15, 88, 2),
-- Recent 2026: Rohit Sharma & Virat Kohli (pos 1 & 2)
(35, 2, 1, 2, 126, 1),
-- Historical stands
(27, 1, 3, 10, 120, 3),
(28, 1, 1, 2, 115, 1);
