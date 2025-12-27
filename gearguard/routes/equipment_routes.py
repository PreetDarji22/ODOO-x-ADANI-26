from flask import Blueprint, render_template, request, redirect, url_for
from models.equipment_model import get_all_equipment, add_equipment
from models.team_model import get_all_teams
from models.equipment_model import get_all_equipment
from models.request_model import get_all_requests
from models.team_model import get_all_teams

equipment_bp = Blueprint('equipment', __name__, url_prefix='/equipment')

@equipment_bp.route('/')
def list_equipment():
    # Get all equipment first
    equipment_list = get_all_equipment()
    
    # SEARCH LOGIC: Check if user typed in the search box
    search_query = request.args.get('q')
    
    if search_query:
        search_query = search_query.lower()
        # Filter list: Keep item if Name OR Serial Number contains the search text
        equipment_list = [
            e for e in equipment_list 
            if search_query in e['name'].lower() or search_query in e['serial_number'].lower()
        ]

    return render_template('equipment/list.html', equipment=equipment_list)
    

@equipment_bp.route('/add', methods=['GET', 'POST'])
def add_new_equipment():
    if request.method == 'POST':
        name = request.form['name']
        serial = request.form['serial_number']
        dept = request.form['department']
        loc = request.form['location']
        team_id = request.form['team_id']
        add_equipment(name, serial, dept, loc, team_id)
        return redirect(url_for('equipment.list_equipment'))
    
    # PASS TEAMS TO THE TEMPLATE
    all_teams = get_all_teams()
    return render_template('equipment/add.html', teams=all_teams)

@equipment_bp.route('/<eq_id>')
def view_equipment(eq_id):
    # 1. Find the specific equipment
    all_eq = get_all_equipment()
    equipment = next((item for item in all_eq if item['id'] == eq_id), None)
    
    if not equipment:
        return "Equipment not found", 404

    # 2. Find all requests for this equipment (Smart Button Logic)
    all_reqs = get_all_requests()
    equipment_requests = [r for r in all_reqs if r['equipment_id'] == eq_id]
    request_count = len(equipment_requests)

    return render_template('equipment/view.html', equipment=equipment, request_count=request_count)