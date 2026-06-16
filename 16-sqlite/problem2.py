# Write a function insert_records(db_path, table_name, records) that:

# Takes a database path, table name, and a list of dictionaries (each dict is one row)
# Inserts all records into the table using executemany()
# Returns the number of rows inserted
# Returns 0 if anything goes wrong

import sqlite3

def insert_records(db_path, table_name, records):
    columns = records[0].keys()
    placeholders = ", ".join(["?" for _ in columns])
    query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(query, [tuple(r.values()) for r in records])
            inserted_rows = cursor.rowcount
            conn.commit()
        return inserted_rows
    except sqlite3.Error as e:
        print(f"Database error occurred {e}")
        return 0

print(insert_records("D:/python_practice/16-sqlite/mydb.db", "students", [
    {"name": "Ali", "age": 20, "grade": "A"},
    {"name": "Sara", "age": 22, "grade": "B"},
    {"name": "John", "age": 21, "grade": "A"}
]))
