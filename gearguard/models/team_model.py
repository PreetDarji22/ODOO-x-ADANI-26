from models.db import get_db_connection

def get_all_teams():
    conn = get_db_connection()
    teams = conn.execute('SELECT * FROM teams').fetchall()
    conn.close()
    return [dict(t) for t in teams]

def get_team_by_id(team_id):
    conn = get_db_connection()
    team = conn.execute('SELECT * FROM teams WHERE id = ?', (team_id,)).fetchone()
    conn.close()
    return dict(team) if team else {'id': 0, 'name': 'Unknown', 'description': ''}

def add_team(name, description):
    conn = get_db_connection()
    conn.execute('INSERT INTO teams (name, description) VALUES (?, ?)', (name, description))
    conn.commit()
    conn.close()