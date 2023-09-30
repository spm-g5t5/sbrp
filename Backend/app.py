from flask import Flask
from role.role import role_routes
from staff.staff import staff_routes
from apply.apply import apply_routes

from extensions import db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

app.register_blueprint(role_routes)
app.register_blueprint(staff_routes)
app.register_blueprint(apply_routes)

@app.route('/')
def hello():
    return "Welcome to SBRP"

if __name__ == '__main__':
    app.run(debug=True)

# To obtain parameters from config
# app.config["DB_HOST"] where key = key in config