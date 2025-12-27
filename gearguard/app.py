from flask import Flask, render_template
from routes.equipment_routes import equipment_bp
from routes.team_routes import team_bp
from routes.request_routes import request_bp

app = Flask(__name__)

# Register Blueprints (Connecting the route files to the main app)
app.register_blueprint(equipment_bp)
app.register_blueprint(team_bp)
app.register_blueprint(request_bp)

# Home Page Route (Dashboard)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)