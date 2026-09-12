-- Cricbuzz LiveStats Database Schema (Normalized 3NF)
-- Supports SQLite and standard SQL relational databases

DROP TABLE IF EXISTS batting_partnerships;
DROP TABLE IF EXISTS player_match_fielding;
DROP TABLE IF EXISTS player_match_bowling;
DROP TABLE IF EXISTS player_match_batting;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS series;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS venues;
DROP TABLE IF EXISTS teams;

-- 1. Teams Table
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name VARCHAR(50) NOT NULL UNIQUE,
    short_code VARCHAR(10) NOT NULL UNIQUE,
    country VARCHAR(50) NOT NULL
);

-- 2. Venues Table
CREATE TABLE venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    capacity INTEGER NOT NULL
);

-- 3. Players Table
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    team_id INTEGER NOT NULL,
    playing_role VARCHAR(50) NOT NULL, -- Batsman, Bowler, All-rounder, Wicket-keeper
    batting_style VARCHAR(50) NOT NULL,
    bowling_style VARCHAR(50) NOT NULL,
    debut_year INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- 4. Series Table
CREATE TABLE series (
    series_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_name VARCHAR(100) NOT NULL,
    host_country VARCHAR(50) NOT NULL,
    match_type VARCHAR(20) NOT NULL, -- Test, ODI, T20I
    start_date DATE NOT NULL,
    end_date DATE,
    total_matches INTEGER NOT NULL
);

-- 5. Matches Table
CREATE TABLE matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id INTEGER NOT NULL,
    match_desc VARCHAR(150) NOT NULL,
    team1_id INTEGER NOT NULL,
    team2_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    match_date DATE NOT NULL,
    match_format VARCHAR(20) NOT NULL, -- Test, ODI, T20I
    toss_winner_id INTEGER NOT NULL,
    toss_decision VARCHAR(10) NOT NULL, -- bat, bowl
    match_winner_id INTEGER,
    win_margin INTEGER,
    win_type VARCHAR(20), -- runs, wickets, tie, no result
    match_status VARCHAR(20) DEFAULT 'Completed',
    FOREIGN KEY (series_id) REFERENCES series(series_id),
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (venue_id) REFERENCES venues(venue_id),
    FOREIGN KEY (toss_winner_id) REFERENCES teams(team_id),
    FOREIGN KEY (match_winner_id) REFERENCES teams(team_id)
);

-- 6. Player Match Batting Performance
CREATE TABLE player_match_batting (
    batting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    innings INTEGER NOT NULL, -- 1 or 2
    batting_position INTEGER NOT NULL,
    runs_scored INTEGER NOT NULL DEFAULT 0,
    balls_faced INTEGER NOT NULL DEFAULT 0,
    fours INTEGER DEFAULT 0,
    sixes INTEGER DEFAULT 0,
    strike_rate REAL DEFAULT 0.0,
    is_out INTEGER DEFAULT 1, -- 1 = Out, 0 = Not Out
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- 7. Player Match Bowling Performance
CREATE TABLE player_match_bowling (
    bowling_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    innings INTEGER NOT NULL,
    overs_bowled REAL NOT NULL DEFAULT 0.0,
    maidens INTEGER DEFAULT 0,
    runs_conceded INTEGER NOT NULL DEFAULT 0,
    wickets_taken INTEGER NOT NULL DEFAULT 0,
    economy_rate REAL DEFAULT 0.0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- 8. Player Match Fielding Performance
CREATE TABLE player_match_fielding (
    fielding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    catches INTEGER DEFAULT 0,
    stumpings INTEGER DEFAULT 0,
    run_outs INTEGER DEFAULT 0,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- 9. Batting Partnerships Table
CREATE TABLE batting_partnerships (
    partnership_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    innings INTEGER NOT NULL,
    batsman1_id INTEGER NOT NULL,
    batsman2_id INTEGER NOT NULL,
    partnership_runs INTEGER NOT NULL,
    wicket_number INTEGER NOT NULL,
    FOREIGN KEY (match_id) REFERENCES matches(match_id) ON DELETE CASCADE,
    FOREIGN KEY (batsman1_id) REFERENCES players(player_id),
    FOREIGN KEY (batsman2_id) REFERENCES players(player_id)
);

-- Indexes for High Performance Queries
CREATE INDEX idx_players_team ON players(team_id);
CREATE INDEX idx_players_role ON players(playing_role);
CREATE INDEX idx_matches_date ON matches(match_date);
CREATE INDEX idx_matches_format ON matches(match_format);
CREATE INDEX idx_matches_series ON matches(series_id);
CREATE INDEX idx_batting_player ON player_match_batting(player_id);
CREATE INDEX idx_batting_match ON player_match_batting(match_id);
CREATE INDEX idx_bowling_player ON player_match_bowling(player_id);
CREATE INDEX idx_bowling_match ON player_match_bowling(match_id);
CREATE INDEX idx_partnerships_match ON batting_partnerships(match_id);
