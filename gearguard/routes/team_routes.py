from flask import Blueprint, render_template, request, redirect, url_for
from models.team_model import get_all_teams, add_team

team_bp = Blueprint('teams', __name__, url_prefix='/teams')

@team_bp.route('/')
def list_teams():
    teams = get_all_teams()
    # In a real app, we would count how many technicians are in each team
    return render_template('teams/list.html', teams=teams)

@team_bp.route('/add', methods=['GET', 'POST'])
def add_new_team():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        add_team(name, description)
        return redirect(url_for('teams.list_teams'))
    
    return render_template('teams/add.html')