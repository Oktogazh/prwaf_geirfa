import pytest
import sqlite3
import os

# Assuming your module is named prawf_geirfa and is in the prawf_geirfa package
from prawf_geirfa import your_module_function

DATABASE_PATH = "items.db"


@pytest.fixture(scope="module")
def setup_database():
    # Create a temporary database for testing
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create the item table
    cursor.execute(
        """
    CREATE TABLE item (
        word TEXT,
        isRealWord BOOLEAN,
        rating REAL,
        is_real_word BOOLEAN
    )
    """
    )

    # Insert some sample data
    cursor.execute(
        """
    INSERT INTO item (word, isRealWord, rating, is_real_word)
    VALUES ('example', 1, 5.0, 1)
    """
    )

    conn.commit()
    conn.close()

    yield

    # Clean up the database after tests
    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)


def test_database_connection(setup_database):
    # Assuming your_module_function is the function that connects to the database
    conn = your_module_function()

    assert conn is not None, "Database connection failed"

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='item'")
    table_info = cursor.fetchone()

    assert table_info is not None, "item table does not exist"

    cursor.execute("PRAGMA table_info(item)")
    columns = cursor.fetchall()

    expected_columns = [
        ("word", "TEXT", 0, None, None, None),
        ("isRealWord", "BOOLEAN", 0, None, None, None),
        ("rating", "REAL", 0, None, None, None),
        ("is_real_word", "BOOLEAN", 0, None, None, None),
    ]

    assert (
        columns == expected_columns
    ), "item table columns do not match expected structure"

    conn.close()
