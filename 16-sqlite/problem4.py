# Write a function update_records(db_path, table_name, updates, condition) that:

# Takes a dict of updates (column → new value) and a condition string
# Updates matching records
# Returns the number of rows updated
# Returns 0 if anything goes wrong

import sqlite3
def update_records(db_path, table_name, updates, condition):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
            query_params = list(updates.values())
            query = f"UPDATE {table_name} SET {set_clause}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query, query_params)
            conn.commit()
            return cursor.rowcount
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

print(update_records(
    "D:/python_practice/16-sqlite/mydb.db",
    "students",
    {"grade": "A+", "age": 21},
    "name = 'Ali'"
))