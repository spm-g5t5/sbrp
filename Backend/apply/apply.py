from flask import jsonify, Blueprint, request
from models import Apply, ApplySkill, Role, RoleSkill, StaffSkill, RoleListingSkills
import requests

apply_routes = Blueprint('apply_routes', __name__)

#get all applications
@apply_routes.route('/API/v1/viewApplicants')
def viewApplicants():
    try:
        processed_applications = []
        applications = Apply.query.all()
        

        if not applications:
            # If there are no applications, return a 200 Not Found status
            return jsonify({"error": "No applicants found"}), 200
        
        # for each applicants found
        for applicant in applications:
            temp_application = applicant.json()  # Call json() on the individual applicant
            temp_application['staff'] = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/{applicant.json()["applicant_staff_id"]}').json()
            

            role = Role.query.filter_by(role_id=applicant.json()["applied_role_id"]).first()
            temp_application['role'] = role.json()

            role_id = role.json()["role_id"]
            role_skills = RoleListingSkills.query.filter_by(role_id=role_id).all()
            temp_application['role_skills'] = [skill.json() for skill in role_skills]
            
            staff_skill = StaffSkill.query.filter_by(staff_id=applicant.json()["applicant_staff_id"]).all()
            temp_application['staff_skill'] = [skill.json() for skill in staff_skill]


            processed_applications += [temp_application]
       

        return jsonify(processed_applications), 200
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

