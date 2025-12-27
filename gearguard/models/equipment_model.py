from models.db import get_db_connection

def get_all_equipment():
    conn = get_db_connection()
    query = '''
        SELECT equipment.*, teams.name as team_name 
        FROM equipment 
        LEFT JOIN teams ON equipment.team_id = teams.id
    '''
    equipment = conn.execute(query).fetchall()
    conn.close()
    return [dict(row) for row in equipment]

def add_equipment(name, serial_number, department, location, team_id):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO equipment (name, serial_number, department, location, team_id, status)
        VALUES (?, ?, ?, ?, ?, 'Operational')
    ''', (name, serial_number, department, location, team_id))
    conn.commit()
    conn.close()

def set_equipment_scrap(eq_id):
    conn = get_db_connection()
    conn.execute("UPDATE equipment SET status = 'Scrapped' WHERE id = ?", (eq_id,))
    conn.commit()
    conn.close()