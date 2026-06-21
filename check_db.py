from app import app, db
from models import GameSession

with app.app_context():
    sessions = GameSession.query.all()
    for s in sessions:
        print(f'ID: {s.id}, JoinCode: {s.join_code}')
