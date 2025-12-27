from models.db import get_db_connection

def get_all_requests():
    conn = get_db_connection()
    query = '''
        SELECT requests.*, equipment.name as equipment_name 
        FROM requests 
        LEFT JOIN equipment ON requests.equipment_id = equipment.id
    '''
    reqs = conn.execute(query).fetchall()
    conn.close()
    return [dict(row) for row in reqs]

def get_request_by_id(req_id):
    conn = get_db_connection()
    query = '''
        SELECT requests.*, equipment.name as equipment_name 
        FROM requests 
        LEFT JOIN equipment ON requests.equipment_id = equipment.id
        WHERE requests.id = ?
    '''
    req = conn.execute(query, (req_id,)).fetchone()
    conn.close()
    return dict(req) if req else None

def create_request(subject, request_type, equipment_id, scheduled_date):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO requests (subject, request_type, equipment_id, scheduled_date, stage)
        VALUES (?, ?, ?, ?, 'New')
    ''', (subject, request_type, equipment_id, scheduled_date))
    conn.commit()
    conn.close()

def update_request_stage(req_id, new_stage, duration, note):
    conn = get_db_connection()
    conn.execute('''
        UPDATE requests 
        SET stage = ?, duration = ?, resolution_note = ?
        WHERE id = ?
    ''', (new_stage, duration, note, req_id))
    conn.commit()
    conn.close()