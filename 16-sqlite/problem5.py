# Write a function delete_records(db_path, table_name, condition) that:

# Deletes records matching the condition
# If condition is None, deletes all records
# Returns the number of rows deleted
# Returns 0 if anything goes wrong

import sqlite3
def delete_records(db_path, table_name, condition):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {table_name}"
            if condition:
                query += f" WHERE {condition}"
            cursor.execute(query)
            conn.commit()
            return cursor.rowcount    
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return 0
    
print(delete_records("D:/python_practice/16-sqlite/mydb.db", "students", "grade = 'B'"))