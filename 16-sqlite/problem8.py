# Write a function export_to_csv(db_path, table_name, output_csv_path) that:

# Fetches all records from the table
# Writes them to a CSV file with column headers
# Returns the number of rows exported
# Returns 0 if anything goes wrong

import csv
import sqlite3

def export_to_csv(db_path, table_name, output_csv_path):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            column_names = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
        with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(column_names)
            writer.writerows(rows)
            return len(rows)
    except Exception as e:
        print(f"Error occurred {e}")
        return 0
    
print(export_to_csv("D:/python_practice/16-sqlite/mydb.db", "students", "D:/python_practice/16-sqlite/students.csv"))

        