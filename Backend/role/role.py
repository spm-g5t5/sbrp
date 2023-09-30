from flask import jsonify, Blueprint, current_app
from models import Role, RoleSkill

role_routes = Blueprint('role_routes', __name__)

#get all roles
@role_routes.route('/API/v1/viewRoles')
def viewRoles():
    try:
        roles = Role.query.all()
        if not roles:
            # If there are no roles found, return a 404 Not Found status
            return jsonify({"error": "No roles found"}), 200

        # Return a JSON response with the list of roles
        return jsonify([role.json() for role in roles]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get skills needed for a specific role
@role_routes.route('/API/v1/viewRoles/skill/<string:name>')
def getSkillsByRoleName(name):
    try:
        role_name = RoleSkill.query.filter_by(role_name=name).all()
        if not role_name:
            # If there are no skills found for the specified role name, return a 404 Not Found status
            return jsonify({"error": "No skills found for this role name"}), 200

        # Return a JSON response with the list of skills for the specified role name
        return jsonify([role.json() for role in role_name]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500