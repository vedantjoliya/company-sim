import sqlite3
import os
db_path = os.path.join('instance', 'company_sim.db')
if not os.path.exists(db_path):
    print("DB doesn't exist at", db_path)
else:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, join_code FROM game_session")
        rows = cur.fetchall()
        for r in rows:
            print(r)
    except Exception as e:
        print("Error:", e)
