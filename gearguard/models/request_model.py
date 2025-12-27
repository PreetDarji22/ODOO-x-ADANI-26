# MOCK DATABASE
REQUESTS_DB = []

def get_all_requests():
    return REQUESTS_DB

def get_request_by_id(req_id):
    # Find the specific request dictionary
    for req in REQUESTS_DB:
        if req['id'] == str(req_id):
            return req
    return None

def create_request(subject, request_type, equipment_id, scheduled_date):
    new_id = str(len(REQUESTS_DB) + 1)
    
    # Mock lookup for equipment name (in a real DB, we use JOIN)
    # This is just for display purposes in the list
    eq_name = "Unknown Machine" 
    from models.equipment_model import get_all_equipment
    all_eq = get_all_equipment()
    for eq in all_eq:
        if eq['id'] == str(equipment_id):
            eq_name = eq['name']
            break

    new_req = {
        'id': new_id,
        'subject': subject,
        'request_type': request_type,
        'equipment_id': equipment_id,
        'equipment_name': eq_name,
        'scheduled_date': scheduled_date,
        'stage': 'New',           # [cite: 42] Starts as New
        'duration': 0.0,          # [cite: 45] Duration field
        'resolution_note': ''
    }
    REQUESTS_DB.append(new_req)

def update_request_stage(req_id, new_stage, duration, note):
    req = get_request_by_id(req_id)
    if req:
        req['stage'] = new_stage
        req['duration'] = duration
        req['resolution_note'] = note