from flask import jsonify, Blueprint, current_app, request
from models import Role, RoleSkill
from datetime import datetime
from models import db

role_routes = Blueprint('role_routes', __name__)

#get all roles
@role_routes.route('/API/v1/viewRoles')
def viewRoles():
    try:
        roles = Role.query.all()
        if not roles:
            # If there are no roles found, return a 200 Not Found status
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
            # If there are no skills found for the specified role name, return a 200 Not Found status
            return jsonify({"error": "No skills found for this role name"}), 200

        # Return a JSON response with the list of skills for the specified role name
        return jsonify([role.json() for role in role_name]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#search for role by name
@role_routes.route('/API/v1/searchRole/<string:inputRoleName>')
def getRolebyName(inputRoleName):
    try:
        inputRoleName = "%{}%".format(inputRoleName)
        role_search_results = Role.query.filter(Role.role_name.like(inputRoleName)).all()
        if not role_search_results:
            return jsonify({"error": "No role found with search criteria"}), 200

        return jsonify([role.json() for role in role_search_results]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#create a new role
@role_routes.route('/API/v1/createRole', methods=['POST'])
def addRole():
    try:
        data = request.get_json()

        # Convert the 'expiry_dt' string to a datetime object
        expiry_dt = datetime.strptime(data['expiry_dt'], '%Y-%m-%d')  # Adjust the format as needed

        # Create a new role record
        new_role = Role(
            role_id=None,
            role_name=data['role_name'],
            job_type=data['job_type'],
            department=data['department'],
            job_description=data['job_description'],
            original_creation_dt=datetime.now(),
            expiry_dt=expiry_dt,
            hiring_manager_id=data['hiring_manager_id']
        )
        
        # Create a list to store the RoleSkill records
        role_skills = []

        # Loop through the list of skills and create RoleSkill records
        for skill_name in data['role_skills']:
            role_skill = RoleSkill(
                role_name=data['role_name'],
                skill_name=skill_name
            )
            role_skills.append(role_skill)

        # Add the RoleSkill records to the session
        db.session.add_all(role_skills)

        # Add the new role to the session
        db.session.add(new_role)
  
        # Commit the session to persist the record in the database
        db.session.commit()

        response_data = {
            "role": new_role.json(),
            "role_skills": [role_skill.json() for role_skill in role_skills]
        }

        return jsonify(response_data), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        return f"Error inserting data: {str(e)}", 500