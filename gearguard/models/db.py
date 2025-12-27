import sqlite3
import os

# 1. Get the path to the main 'gearguard' folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 2. Join it with the database filename
DB_PATH = os.path.join(BASE_DIR, 'gearguard.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn