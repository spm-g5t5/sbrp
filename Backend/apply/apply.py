from flask import jsonify, Blueprint, request
from models import Apply, ApplySkill, Role, RoleSkill, StaffSkill, RoleListingSkills, db
from datetime import datetime
import requests

apply_routes = Blueprint('apply_routes', __name__)

#get all applications
@apply_routes.route('/API/v1/viewApplicants', methods=['GET', 'POST'])
def viewApplicants():
    try:
        inputSkillsLst = []

        if request.method == "POST":
            resp = request.get_json()

            if "skills" in resp:
                if resp['skills'] != []:
                    inputSkillsLst = resp['skills']

        processed_applications = []
        applications = Apply.query.all()
        
        if not applications:
            # If there are no applications, return a 200 Not Found status
            return jsonify({"error": "No applicants found"}), 200
        
        # for each applicants found
        for applicant in applications:
            skill_match_lst = []
            temp_application = applicant.json()  # Call json() on the individual applicant
            temp_application['staff'] = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/{applicant.json()["applicant_staff_id"]}').json()
            
            role = Role.query.filter_by(role_id=applicant.json()["applied_role_id"]).first()
            temp_application['role'] = role.json()

            # Query role listing skills
            role_id = role.json()["role_id"]
            subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
            query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
            role_skills = query.filter_by(role_id=role_id).all()
            temp_application['role_skills'] = [skill.json() for skill in role_skills]
            
            staff_skill = StaffSkill.query.filter_by(staff_id=applicant.json()["applicant_staff_id"]).all()
            temp_application['staff_skill'] = [skill.json() for skill in staff_skill]

            for staff_skill in temp_application['staff_skill']:
                for skill in inputSkillsLst:
                    if staff_skill['skill_name'] == skill:
                        skill_match_lst.append(staff_skill['skill_name'])

            if len(inputSkillsLst) == len(skill_match_lst):
                temp_application['skill_matched'] = skill_match_lst
                temp_application['skill_matched_count'] = len(skill_match_lst)
                processed_applications += [temp_application]       

        return jsonify(processed_applications), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get applications for a specfic role
@apply_routes.route('/API/v1/viewApplicants/role/<int:id>', methods=['GET', 'POST'])
def getApplicantByRoleId(id):
    
    try:
        inputSkillsLst = []

        if request.method == "POST":
            resp = request.get_json()

            if "skills" in resp:
                if resp['skills'] != []:
                    inputSkillsLst = resp['skills']

        processed_applications = []
        applications = Apply.query.filter_by(applied_role_id=id).all()

        if not applications:
            # If there are no applicants for the specified role, return a 200 Not Found status
            return jsonify({"error": "No applicants found for this role"}), 200
        
        for applicant in applications:
            skill_match_lst = []
            temp_application = applicant.json()  # Call json() on the individual applicant
            temp_application['staff'] = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/{applicant.json()["applicant_staff_id"]}').json()
            

            role = Role.query.filter_by(role_id=applicant.json()["applied_role_id"]).first()
            temp_application['role'] = role.json()

            # Query role listing skills
            role_id = role.json()["role_id"]
            subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
            query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
            role_skills = query.filter_by(role_id=role_id).all()
            temp_application['role_skills'] = [skill.json() for skill in role_skills]
            
            staff_skill = StaffSkill.query.filter_by(staff_id=applicant.json()["applicant_staff_id"]).all()
            temp_application['staff_skill'] = [skill.json() for skill in staff_skill]

            for staff_skill in temp_application['staff_skill']:
                for skill in inputSkillsLst:
                    if staff_skill['skill_name'] == skill:
                        skill_match_lst.append(staff_skill['skill_name'])

            if len(inputSkillsLst) == len(skill_match_lst):
                temp_application['skill_matched'] = skill_match_lst
                temp_application['skill_matched_count'] = len(skill_match_lst)
                processed_applications += [temp_application]       

        

        # Return a JSON response with the list of applicants for the specified role
        return jsonify(processed_applications), 200
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

@apply_routes.route('/API/v1/createApplication', methods=['POST'])
def createApplication():
    try:
        resp = request.get_json()
        inputStaffId = resp['staff_id']
        inputRoleId = resp['role_id']

        roles = requests.get(f'{request.url_root.rstrip("/")}/API/v1/viewRoles/{inputRoleId}').json()
        if 'error' in roles:
            return jsonify({"error": "Role does not exist"}), 200
        else:
            if roles[0]['active_status'] == True:
                results = Apply.query.filter_by(applicant_staff_id = inputStaffId, applied_role_id = inputRoleId).all()
                if len(results) == 0:

                    staff = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/{inputStaffId}').json()
                    staff_role = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/getstaffrole/{inputStaffId}').json()
                    
                    if 'role_name' in staff_role:
                        inputStaffRole = staff_role['role_name']
                        if (roles[0]['role_name'].lower() == staff_role['role_name'].lower()) and (roles[0]['department'].lower() == staff['dept'].lower()):
                            return jsonify({"error": "Applicant cannot apply for a role which is the same role and department as they currently are in now"}), 200
                    else:
                        inputStaffRole = ""
                    # Create a new role record
                    new_app = Apply(
                        application_id= None,
                        applicant_staff_id = inputStaffId,
                        applicant_existing_role = inputStaffRole,
                        applicant_existing_dept = staff['dept'],
                        application_status = "PENDING",
                        date_applied = datetime.now(),
                        applied_role_id = inputRoleId,
                        applied_role_ver = roles[0]['role_listing_ver']
                        )

                    # Add the new role to the session
                    db.session.add(new_app)
                    db.session.commit()
                    # Return a JSON response with the list of applicants for the specified skill ID
                    return jsonify([new_app.json()]), 200
                else:
                    return jsonify({"error": "Application already exists"}), 200
            else: 
                return jsonify({"error": "Role is not active"}), 200
    
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500


@apply_routes.route('/API/v1/getStaffApplication', methods=['POST'])
def getStaffApplication():
    try:
        resp = request.get_json()
        inputStaffId = resp['staff_id']

        results = Apply.query.filter_by(applicant_staff_id=inputStaffId).with_entities(Apply.applied_role_id).all()
        flattened_results = [item[0] for item in results]
        print(flattened_results)
        return jsonify(flattened_results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


    