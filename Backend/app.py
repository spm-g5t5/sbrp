from flask import Flask
from role.role import role_routes
from staff.staff import staff_routes
from apply.apply import apply_routes
from role_skill_match.role_skill_match import rs_match_routes
from database.database import database_routes
from flask_cors import CORS

from extensions import db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
CORS(app)

app.register_blueprint(role_routes)
app.register_blueprint(staff_routes)
app.register_blueprint(apply_routes)
app.register_blueprint(rs_match_routes)
app.register_blueprint(database_routes)

@app.route('/')
def hello():
    return "Welcome to SBRP"

if __name__ == '__main__':
    app.run(debug=True)