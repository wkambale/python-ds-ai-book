import pandas as pd
import sqlite3

def load_data_as_dataframe(db_path: str, query: str) -> pd.DataFrame:
    """
    Executes a SQL query and returns results as a pandas DataFrame.

    Args:
        db_path: Path to the SQLite database file.
        query: SQL query string to execute.

    Returns:
        DataFrame containing the query results.
    """
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql_query(query, conn)

# Load all students into a DataFrame
df = load_data_as_dataframe(
    'practice.db',
    "SELECT * FROM students ORDER BY score DESC;"
)

print(df)
print(f"\nDataFrame shape: {df.shape}")
print(f"Column types:\n{df.dtypes}")