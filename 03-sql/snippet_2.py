import sqlite3

def get_all_students(db_path: str) -> list:
    """Safely fetches all students using a context manager."""
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students ORDER BY score DESC;")
        return cur.fetchall()
    # Connection is automatically closed when exiting the 'with' block

students = get_all_students('practice.db')
for student in students:
    print(f"ID: {student[0]}, Name: {student[1]}, Score: {student[2]}")