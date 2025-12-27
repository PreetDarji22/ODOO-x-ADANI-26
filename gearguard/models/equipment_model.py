from models.team_model import get_team_by_id

# MOCK DATABASE
EQUIPMENT_DB = [
    # Dummy data to start with
    {
        'id': '1', 
        'name': 'CNC Machine 01', 
        'serial_number': 'CNC-99', 
        'location': 'Factory Floor', 
        'department': 'Production',
        'team_id': '1'
    }
]

def get_all_equipment():
    # We need to manually "join" the team name here for the display
    results = []
    for item in EQUIPMENT_DB:
        team = get_team_by_id(item['team_id'])
        # Create a copy of the item and add the team name to it
        item_with_team = item.copy()
        item_with_team['team_name'] = team['name']
        results.append(item_with_team)
    return results

def add_equipment(name, serial_number, department, location, team_id):
    new_id = str(len(EQUIPMENT_DB) + 1) # Generate a fake ID
    new_item = {
        'id': new_id,
        'name': name,
        'serial_number': serial_number,
        'department': department,
        'location': location,
        'team_id': team_id
    }
    EQUIPMENT_DB.append(new_item)