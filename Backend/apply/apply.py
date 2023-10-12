from flask import jsonify, Blueprint
from models import Apply, ApplySkill

apply_routes = Blueprint('apply_routes', __name__)

#get all applications
@apply_routes.route('/API/v1/viewApplicants')
def viewApplicants():
    try:
        applications = Apply.query.all()
        if not applications:
            # If there are no applications, return a 200 Not Found status
            return jsonify({"error": "No applicants found"}), 200

        # Return a JSON response with the list of applicants
        return jsonify([app.json() for app in applications]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get applications for a specfic role
@apply_routes.route('/API/v1/viewApplicants/role/<int:id>')
def getApplicantByRoleId(id):
    try:
        applications = Apply.query.filter_by(applied_role_id=id).all()
        if not applications:
            # If there are no applicants for the specified role, return a 200 Not Found status
            return jsonify({"error": "No applicants found for this role"}), 200

        # Return a JSON response with the list of applicants for the specified role
        return jsonify([app.json() for app in applications]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get applications for a specific application
@apply_routes.route('/API/v1/viewApplicants/application/<int:id>')
def getApplicantByApplicationId(id):
    try:
        applications = Apply.query.filter_by(application_id=id).all()
        if not applications:
            # If there are no applicants for the specified application ID, return a 200 Not Found status
            return jsonify({"error": "No applicants found for this application ID"}), 200

        # Return a JSON response with the list of applicants for the specified application ID
        return jsonify([app.json() for app in applications]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get skill of a specific application
@apply_routes.route('/API/v1/viewApplicants/skill/<int:id>')
def getApplicantBySkillId(id):
    try:
        applications = ApplySkill.query.filter_by(application_id=id).all()
        if not applications:
            # If there are no applicants for the specified skill ID, return a 200 Not Found status
            return jsonify({"error": "No applicants found for this skill ID"}), 200

        # Return a JSON response with the list of applicants for the specified skill ID
        return jsonify([app.json() for app in applications]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

