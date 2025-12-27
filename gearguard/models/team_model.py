# MOCK DATABASE
TEAMS_DB = [
    {'id': '1', 'name': 'Mechanical Team', 'description': 'Fixes heavy machinery and motors.'},
    {'id': '2', 'name': 'IT Support', 'description': 'Handles computers, screens, and software.'},
    {'id': '3', 'name': 'Facility Maint.', 'description': 'General building repairs and lighting.'}
]

def get_all_teams():
    return TEAMS_DB

def get_team_by_id(team_id):
    for team in TEAMS_DB:
        if team['id'] == str(team_id):
            return team
    return {'id': '0', 'name': 'Unknown Team', 'description': ''}

def add_team(name, description):
    new_id = str(len(TEAMS_DB) + 1)
    new_team = {
        'id': new_id,
        'name': name,
        'description': description
    }
    TEAMS_DB.append(new_team)