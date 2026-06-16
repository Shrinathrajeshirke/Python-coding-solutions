# Write a function create_database(db_path, table_name, columns) that:

# Takes a database file path, a table name, and a dictionary of columns where keys are column names and values are data types (e.g. "TEXT", "INTEGER")
# Creates the database and table if they don't exist
# Always includes an id column as INTEGER PRIMARY KEY AUTOINCREMENT
# Returns True if successful, False if anything goes wrong

import sqlite3

def create_database(db_path, table_name, columns):
    cols = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        {cols}
                        )""")
            conn.commit()
            return True
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
        return False
    
print(create_database(
    "D:/python_practice/16-sqlite/mydb.db",
    "students",
    {"name": "TEXT", "age": "INTEGER", "grade": "TEXT"}
))
        