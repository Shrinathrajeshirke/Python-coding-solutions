# Write a function merge_databases(db1_path, db2_path, table_name, output_db_path) that:

# Reads all records from table_name in both databases
# Merges them into a new database at output_db_path
# Creates the table in the output database with the same structure
# Returns the total number of rows in the merged database
# Returns 0 if anything goes wrong

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

import sqlite3

def merge_databases(db1_path, db2_path, table_name, output_db_path):
    try:
        with sqlite3.connect(output_db_path) as conn:
            cursor = conn.cursor()
            
            # Attach both databases
            cursor.execute(f"ATTACH DATABASE '{db1_path}' AS db1")
            cursor.execute(f"ATTACH DATABASE '{db2_path}' AS db2")
            
            # Get table structure from db1
            cursor.execute(f"SELECT sql FROM db1.sqlite_master WHERE type='table' AND name='{table_name}'")
            create_table_sql = cursor.fetchone()[0]
            create_table_sql = create_table_sql.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS")
            cursor.execute(create_table_sql)
            
            # Get column names except 'id'
            cursor.execute(f"PRAGMA db1.table_info({table_name})")
            columns = [row[1] for row in cursor.fetchall() if row[1] != "id"]
            cols = ", ".join(columns)

            # Insert without id — let AUTOINCREMENT handle it
            cursor.execute(f"INSERT INTO {table_name} ({cols}) SELECT {cols} FROM db1.{table_name}")
            cursor.execute(f"INSERT INTO {table_name} ({cols}) SELECT {cols} FROM db2.{table_name}")
            
            conn.commit()
            
            # Get total rows
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            total_rows = cursor.fetchone()[0]
            
            cursor.execute("DETACH DATABASE db1")
            cursor.execute("DETACH DATABASE db2")
            
            return total_rows
    
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return 0
    
create_database(
    "D:/python_practice/16-sqlite/db1.db",
    "students",
    {"name": "TEXT", "age": "INTEGER", "grade": "TEXT"}
)

create_database(
    "D:/python_practice/16-sqlite/db2.db",
    "students",
    {"name": "TEXT", "age": "INTEGER", "grade": "TEXT"}
)

create_database(
    "D:/python_practice/16-sqlite/merged.db",
    "students",
    {"name": "TEXT", "age": "INTEGER", "grade": "TEXT"}
)

insert_records("D:/python_practice/16-sqlite/db1.db", "students", [
    {"name": "Ali", "age": 20, "grade": "A"},
    {"name": "Sara", "age": 22, "grade": "B"},
    {"name": "John", "age": 21, "grade": "A"}
])

insert_records("D:/python_practice/16-sqlite/db2.db", "students", [
    {"name": "Sam", "age": 20, "grade": "A"},
    {"name": "Tom", "age": 22, "grade": "B"}
])
        
print(merge_databases("db1.db", "db2.db", "students", "merged.db"))