# Write a function search_records(db_path, table_name, column, keyword) that:

# Searches for records where column contains keyword (case-insensitive partial match)
# Returns a list of dictionaries
# Returns empty list if nothing found or error occurs

import sqlite3
def search_records(db_path, table_name, column, keyword):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query_params = f"%{keyword}%"
            query = f"SELECT * FROM {table_name} WHERE {column} LIKE ?"
            cursor.execute(query, (query_params,))
            column_names  = [description[0] for description in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(column_names, row)) for row in rows]
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return []
    
print(search_records("D:/python_practice/16-sqlite/mydb.db", "students", "name", "ali"))

