# Write a function get_table_stats(db_path, table_name) that returns a dictionary with:

# "total_rows" → total number of rows
# "columns" → list of column names
# "sample" → first 3 rows as list of dicts

# Returns None if anything goes wrong.

import sqlite3
def get_table_stats(db_path, table_name):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            return {"total_rows": len(rows),
                    "columns": columns,
                    "sample": [dict(zip(columns, row)) for row in rows[:3]]}
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

print(get_table_stats("D:/python_practice/16-sqlite/mydb.db", "students"))
    

