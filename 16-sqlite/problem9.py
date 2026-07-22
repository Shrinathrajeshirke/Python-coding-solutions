# Write a function import_from_csv(db_path, table_name, csv_path) that:

# Reads a CSV file and inserts all rows into the specified table
# First row is the header (column names)
# Returns the number of rows imported
# Returns 0 if anything goes wrong

import csv
import sqlite3

def import_from_csv(db_path, table_name, csv_path):
    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            records = [row for row in reader]
            
        columns = records[0].keys()
        placeholders = ", ".join(["?" for _ in columns])
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
    
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(query, [tuple(r.values()) for r in records])
            inserted_rows = cursor.rowcount
            conn.commit()
        return inserted_rows
    except sqlite3.Error as e:
        print(f"Database error occurred {e}")
        return 0

print(import_from_csv("D:/python_practice/16-sqlite/mydb.db", "students", "D:/python_practice/16-sqlite/students.csv"))
        