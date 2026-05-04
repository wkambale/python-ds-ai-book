import sqlite3
from typing import Optional
def create_sample_database(db_path: str) -> None:
    """Creates a sample database with a students table."""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            score REAL
        );

create_sample_database('practice.db')