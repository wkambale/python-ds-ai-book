import sqlite3

def create_sample_database(db_path: str) -> None:
    """Creates a sample database with a students table and initial data."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                score REAL
            );
        """)
        cursor.executemany(
            "INSERT OR IGNORE INTO students (student_id, name, score) VALUES (?, ?, ?);",
            [
                (1, "Amina", 92.5),
                (2, "Kwame", 85.0),
                (3, "Chidi", 78.0),
                (4, "Fatima", 95.0),
            ]
        )
        conn.commit()

create_sample_database('practice.db')