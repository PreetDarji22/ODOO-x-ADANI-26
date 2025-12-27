from flask import Blueprint, render_template, request, redirect, url_for
from models.request_model import get_all_requests, create_request, get_request_by_id, update_request_stage
from models.equipment_model import get_all_equipment

request_bp = Blueprint('requests', __name__, url_prefix='/requests')

@request_bp.route('/')
def list_requests():
    reqs = get_all_requests()
    
    # Check if we need to filter by equipment (from the Smart Button)
    filter_eq_id = request.args.get('equipment_id')
    if filter_eq_id:
        reqs = [r for r in reqs if r['equipment_id'] == filter_eq_id]

    return render_template('requests/list.html', requests=reqs)

@request_bp.route('/add', methods=['GET', 'POST'])
def add_new_request():
    if request.method == 'POST':
        subject = request.form['subject']
        rtype = request.form['request_type']
        eq_id = request.form['equipment_id']
        date = request.form['scheduled_date']
        create_request(subject, rtype, eq_id, date)
        return redirect(url_for('requests.list_requests'))

    equipment_list = get_all_equipment()
    return render_template('requests/add.html', equipment=equipment_list)

# NEW: Route to View and Edit a specific request
@request_bp.route('/<req_id>', methods=['GET', 'POST'])
def view_request(req_id):
    req = get_request_by_id(req_id)
    
    if not req:
        return "Request not found", 404

    if request.method == 'POST':
        # Update logic [cite: 44-45]
        new_stage = request.form['stage']
        duration = request.form['duration']
        note = request.form['resolution_note']
        
        update_request_stage(req_id, new_stage, duration, note)
        return redirect(url_for('requests.list_requests'))

    return render_template('requests/view.html', req=req)
@request_bp.route('/calendar')
def calendar_view():
    reqs = get_all_requests()
    
    # Transform our internal data into the format FullCalendar needs
    calendar_events = []
    for r in reqs:
        # Set color: Green for Preventive, Red for Corrective
        color = '#10B981' if r['request_type'] == 'Preventive' else '#EF4444'
        
        event = {
            'title': r['subject'],
            'start': r['scheduled_date'], # Must be YYYY-MM-DD
            'url': url_for('requests.view_request', req_id=r['id']), # Click to open details
            'backgroundColor': color,
            'borderColor': color
        }
        calendar_events.append(event)

    return render_template('requests/calendar.html', events=calendar_events)