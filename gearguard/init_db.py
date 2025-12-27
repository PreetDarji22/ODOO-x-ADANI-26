import sqlite3
import os

# Use the exact same path logic as the app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'gearguard.db')

def init_db():
    # CONNECT TO THE ABSOLUTE PATH
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Create Teams
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')

    # 2. Create Equipment
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            serial_number TEXT NOT NULL,
            department TEXT,
            location TEXT,
            team_id INTEGER,
            status TEXT DEFAULT 'Operational',
            FOREIGN KEY (team_id) REFERENCES teams (id)
        )
    ''')

    # 3. Create Requests
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            request_type TEXT NOT NULL,
            equipment_id INTEGER,
            scheduled_date TEXT,
            stage TEXT DEFAULT 'New',
            duration INTEGER DEFAULT 0,
            resolution_note TEXT,
            FOREIGN KEY (equipment_id) REFERENCES equipment (id)
        )
    ''')

    # 4. Create Users (CRITICAL TABLE)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    # 5. Add Data
    cursor.execute('SELECT count(*) FROM teams')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO teams (name, description) VALUES ('Mechanical Team', 'Fixes heavy machinery')")
        cursor.execute("INSERT INTO teams (name, description) VALUES ('IT Support', 'Computers and Screens')")
        print("-> Added default teams.")

    conn.commit()
    conn.close()
    print(f"✅ Database built successfully at: {DB_PATH}")

if __name__ == '__main__':
    init_db()