# Write a function fetch_records(db_path, table_name, condition=None) that:

# Fetches all records from the table
# If condition is provided (as a string), adds it as a WHERE clause
# Returns a list of dictionaries (each row as a dict using column names as keys)
# Returns empty list if anything goes wrong

import sqlite3

def fetch_records(db_path, table_name, condition=None):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query)
            column_names  = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(column_names, row)) for row in rows]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

print(fetch_records("D:/python_practice/16-sqlite/mydb.db", "students", "grade = 'A'"))