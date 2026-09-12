"""
Unit test suite verifying that all 25 SQL queries execute successfully and return non-empty data.
"""
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.connection import initialize_database, execute_query
from sql.query_registry import QUERIES

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    initialize_database()

@pytest.mark.parametrize("query_id", sorted(QUERIES.keys()))
def test_each_sql_query(query_id):
    q_data = QUERIES[query_id]
    sql = q_data["sql"]
    df = execute_query(sql)
    assert df is not None, f"Query {query_id} ({q_data['title']}) returned None"
    assert not df.empty, f"Query {query_id} ({q_data['title']}) returned 0 rows! Expected valid data."
    assert len(df.columns) > 0, f"Query {query_id} returned no columns"
