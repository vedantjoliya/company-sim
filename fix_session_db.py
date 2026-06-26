import sqlite3
import time

db_path = 'instance/company_sim.db'
max_retries = 5

for i in range(max_retries):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("ALTER TABLE game_session ADD COLUMN name TEXT DEFAULT 'Acme Corp'")
        conn.commit()
        conn.close()
        print("Successfully added name column!")
        break
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Column already exists!")
            break
        elif "database is locked" in str(e):
            print("Database is locked, retrying...")
            time.sleep(1)
        else:
            print(f"Error: {e}")
            break
