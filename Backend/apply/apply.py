from flask import jsonify, Blueprint, current_app
from models import Apply

apply_routes = Blueprint('apply_routes', __name__)

@apply_routes.route('/viewApplicants')
def viewApplicants():
    applications = Apply.query.all()
    return jsonify([app.json() for app in applications])

# for config testing
@apply_routes.route('/test/configtest')
def testConfigTest():
    return current_app.config["DB_HOST"] 