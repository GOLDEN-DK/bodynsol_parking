import sqlite3
from pathlib import Path

class DatabaseService:
    def __init__(self):
        self.db_path = Path(__file__).parent.parent / 'db' / 'database.db'
        self.init_db()
    
    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # requests 테이블 생성
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_number TEXT,
            parking_time INTEGER,
            request_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT,
            result_message TEXT
        )
        ''')
        
        # session 테이블 생성
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS session (
            id INTEGER PRIMARY KEY,
            cookie TEXT,
            last_login DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        conn.close() 