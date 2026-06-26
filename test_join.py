import urllib.request
import urllib.parse
import json
import sqlite3


req = urllib.request.Request('http://localhost:5000/create_session', data=json.dumps({'goal_revenue': 1000}).encode('utf-8'), headers={'Content-Type': 'application/json'})
with urllib.request.urlopen(req) as response:
    print("Create response:", response.status, response.read().decode('utf-8'))

conn = sqlite3.connect('instance/company_sim.db')
cur = conn.cursor()
cur.execute("SELECT join_code FROM game_session ORDER BY created_at DESC LIMIT 1")
row = cur.fetchone()
if row:
    join_code = row[0]
    print(f"Latest join code in DB: {join_code}")
    
    join_data = json.dumps({'name': 'TestUser', 'join_code': join_code, 'role_id': 1}).encode('utf-8')
    req2 = urllib.request.Request('http://localhost:5000/join', data=join_data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req2) as response2:
        print("Join response:", response2.status, response2.read().decode('utf-8'))
else:
    print("No sessions found in DB!")
