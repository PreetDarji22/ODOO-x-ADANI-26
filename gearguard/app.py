from flask import Flask, render_template, session, redirect, url_for, request
from routes.equipment_routes import equipment_bp
from routes.team_routes import team_bp
from routes.request_routes import request_bp
from routes.auth_routes import auth_bp
from models.equipment_model import get_all_equipment
from models.request_model import get_all_requests

app = Flask(__name__)
app.secret_key = "change_this_to_something_secret"  # Required for Login

app.register_blueprint(equipment_bp)
app.register_blueprint(team_bp)
app.register_blueprint(request_bp)
app.register_blueprint(auth_bp)

# Force login for all pages except login/signup
@app.before_request
def require_login():
    allowed_routes = ['auth.login', 'auth.signup', 'static']
    if 'user_id' not in session and request.endpoint not in allowed_routes:
        return redirect(url_for('auth.login'))

@app.route('/')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    all_eq = get_all_equipment()
    all_reqs = get_all_requests()

    total_assets = len(all_eq)
    active_requests = [r for r in all_reqs if r['stage'] in ['New', 'In Progress']]
    attention_count = len(active_requests)
    completed_jobs = [r for r in all_reqs if r['stage'] == 'Repaired']
    completed_count = len(completed_jobs)
    total_jobs = len(all_reqs)
    efficiency = int((completed_count / total_jobs * 100)) if total_jobs > 0 else 100

    return render_template('dashboard.html', 
                           total_assets=total_assets,
                           attention_count=attention_count,
                           completed_count=completed_count,
                           efficiency=efficiency,
                           recent_requests=all_reqs[-3:])

if __name__ == '__main__':
    app.run(debug=True, port=5000)