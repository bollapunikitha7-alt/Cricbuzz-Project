"""
Centralized Database Connection Manager for Cricbuzz LiveStats.
Provides thread-safe connections, query execution helpers returning DataFrames,
and automated schema initialization.
"""
import sqlite3
import pandas as pd
from pathlib import Path
import config

def get_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(config.DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def execute_query(query: str, params: tuple = ()) -> pd.DataFrame:
    """
    Execute a SELECT query and return results as a Pandas DataFrame.
    
    Args:
        query: SQL SELECT query string.
        params: Tuple of query parameters to prevent SQL injection.
    
    Returns:
        pd.DataFrame containing the query results.
    """
    conn = get_connection()
    try:
        df = pd.read_sql_query(query, conn, params=params)
        return df
    finally:
        conn.close()

def execute_non_query(query: str, params: tuple = ()) -> int:
    """
    Execute an INSERT, UPDATE, or DELETE query and return the last row ID.
    
    Args:
        query: SQL non-query string.
        params: Tuple of query parameters.
        
    Returns:
        int: The last inserted row ID or affected row count.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.lastrowid if cursor.lastrowid else cursor.rowcount
    finally:
        conn.close()

def initialize_database(force: bool = False):
    """
    Initialize database schema and populate seed data if not already present.
    
    Args:
        force: If True, re-executes schema.sql and seed_data.sql from scratch.
    """
    db_file = Path(config.DB_PATH)
    needs_init = force or not db_file.exists()
    
    conn = get_connection()
    try:
        # Check if tables exist
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='players'")
        has_tables = cursor.fetchone()[0] > 0
        
        if needs_init or not has_tables:
            schema_path = config.DATABASE_DIR / "schema.sql"
            seed_path = config.DATABASE_DIR / "seed_data.sql"
            
            if schema_path.exists():
                with open(schema_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
            
            if seed_path.exists():
                with open(seed_path, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
            print("Database initialized with schema and seed data.")
    finally:
        conn.close()
