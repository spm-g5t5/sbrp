from flask import jsonify, Blueprint
from models import Apply, ApplySkill

apply_routes = Blueprint('apply_routes', __name__)

#get all applications
@apply_routes.route('/API/v1/viewApplicants')
def viewApplicants():
    applications = Apply.query.all()
    return jsonify([app.json() for app in applications])

#get applications for a specfic role
@apply_routes.route('/API/v1/viewApplicants/role/<int:id>')
def getApplicantByRoleId(id):
    applications = Apply.query.filter_by(applied_role_id=id)
    return jsonify([app.json() for app in applications])

#get applications for a sepecfic application
@apply_routes.route('/API/v1/viewApplicants/application/<int:id>')
def getApplicantByApplicationId(id):
    applications = Apply.query.filter_by(application_id=id)
    return jsonify([app.json() for app in applications])

#get skill of a specific application
@apply_routes.route('/API/v1/viewApplicants/skill/<int:id>')
def getApplicantBySkillId(id):
    applications = ApplySkill.query.filter_by(application_id=id)
    return jsonify([app.json() for app in applications])

