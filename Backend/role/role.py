from flask import jsonify, Blueprint, current_app, request
from models import Role, RoleListingSkills, RoleSkill
from datetime import datetime
from models import db
import requests

role_routes = Blueprint('role_routes', __name__)

#get all roles for admin
@role_routes.route('/API/v1/viewRoles')
def viewRoles(): 
    try:
        subquery = db.session.query(Role.role_id, db.func.max(Role.role_listing_ver).label('max_ver')).group_by(Role.role_id).subquery()
        query = db.session.query(Role).join(subquery, db.and_(Role.role_id == subquery.c.role_id, Role.role_listing_ver == subquery.c.max_ver))
        roles = query.all()

        processed_roles = []
        if not roles:
            # If there are no roles found, return a 200 Not Found status
            return jsonify({"error": "No roles found"}), 200
        
        # for each role found
        for role in roles:
            temp_role = role.json()
            temp_role['hiring_manager'] = requests.get(f'{request.url_root.rstrip("/")}/API/v1/staff/{role.json()["hiring_manager_id"]}').json()
            processed_roles += [temp_role]

            # Return a JSON response with the list of roles
        return jsonify(processed_roles), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#get skills needed for a specific role
@role_routes.route('/API/v1/viewRoles/skill/<string:inputRoleID>')
def getSkillsByRoleName(inputRoleID):
    try:

        subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
        query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
        skills = query.filter_by(role_id=inputRoleID).all()

        if not skills:
            # If there are no skills found for the specified role name, return a 200 Not Found status
            return jsonify({"error": "No skills found for this role name"}), 200

        # Return a JSON response with the list of skills for the specified role name
        return jsonify([skill.json() for skill in skills]), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500

#search for role by name
@role_routes.route('/API/v1/searchRole', methods=['POST'])
def getRolebyName():
    try:
        resp = request.get_json()
        inputSkillsLst = []
        inputRoleName = "%{}%".format("")

        if "skills" in resp:
            inputSkillsLst = resp['skills']
        
        if "search" in resp:
            inputRoleName = "%{}%".format(resp['search'])

        subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
        query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
        
        if len(inputSkillsLst) == 0:
            skills = query.all()
        else:
            skills = query.filter(RoleListingSkills.skills.in_(inputSkillsLst)).all()
        
        skills_match = {}

        # Process skills match
        for skill in skills:    
            if skill.json()['role_id'] not in skills_match:
                skills_match[skill.json()['role_id']] = [skill.json()['skill_name']]
            else:
                skills_match[skill.json()['role_id']] += [skill.json()['skill_name']]
                
        # given skills_match dict where i have skills_matched, sort is descending order
        skills_match_desc = dict(sorted(skills_match.items(), key=lambda item: len(item[1]), reverse=True))
        output_processed = []
        for r_id in skills_match_desc:

            subquery = db.session.query(Role.role_id, db.func.max(Role.role_listing_ver).label('max_ver')).group_by(Role.role_id).subquery()
            query = db.session.query(Role).join(subquery, db.and_(Role.role_id == subquery.c.role_id, Role.role_listing_ver == subquery.c.max_ver))
            role = query.filter(Role.role_id == r_id, Role.role_name.like(inputRoleName)).all()
            if len(role) == 1:
                role = role[0]
                role_json = role.json()
                role_json['skills_matched'] = skills_match_desc[r_id]
                role_json['skills_matched_count'] = len(skills_match_desc[r_id])

                output_processed += [role_json]

        if not output_processed:
            return jsonify({"error": "No role found with search criteria"}), 200
        print(output_processed)
        return jsonify(output_processed), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@role_routes.route('/API/v1/role/filter', methods=['POST'])
def getFilter():

    inputSkillsLst = request.get_json()['skills']
    
    try:
        subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
        query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
        skills = query.filter(RoleListingSkills.skills.in_(inputSkillsLst)).all()
        
        skills_match = {}

        # Process skills match
        for skill in skills:    
            if skill.json()['role_id'] not in skills_match:
                skills_match[skill.json()['role_id']] = [skill.json()['skill_name']]
            else:
                skills_match[skill.json()['role_id']] += [skill.json()['skill_name']]
        # given skills_match dict where i have skills_matched, sort is descending order
        skills_match_desc = dict(sorted(skills_match.items(), key=lambda item: len(item[1]), reverse=True))
        output_processed = []
        for r_id in skills_match_desc:

            subquery = db.session.query(Role.role_id, db.func.max(Role.role_listing_ver).label('max_ver')).group_by(Role.role_id).subquery()
            query = db.session.query(Role).join(subquery, db.and_(Role.role_id == subquery.c.role_id, Role.role_listing_ver == subquery.c.max_ver))
            role = query.filter(Role.role_id == r_id).all()[0]

            role_json = role.json()
            role_json['skills_matched'] = skills_match_desc[r_id]
            role_json['skills_matched_count'] = len(skills_match_desc[r_id])

            output_processed += [role_json]

        return jsonify(output_processed), 200
    except Exception as e:

        return f"Error: {str(e)}", 500

    
@role_routes.route('/API/v1/searchAllRoleVer/<string:inputRoleId>')
def getAllRoleVer(inputRoleId):
    try:
        role_search_results = Role.query.filter(Role.role_id == (inputRoleId)).all()
    
        if not role_search_results:
            return jsonify({"error": "No role found with search criteria"}), 200
        
        role = []

        for search_role in role_search_results:
            skill_search_results = RoleListingSkills.query.filter(RoleListingSkills.role_id == (search_role.role_id), RoleListingSkills.role_listing_ver == (search_role.role_listing_ver)).all()
            role += [{
                "role_id": search_role.role_id,
                "role_listing_ver": search_role.role_listing_ver,
                "role": search_role.json(),
                "role_listing_skills": [skill.json() for skill in skill_search_results]
            }]

        return jsonify(role), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
#create a new role
@role_routes.route('/API/v1/createRole', methods=['POST'])
def addRole():
    try:
        data = request.get_json()

        # Convert the 'expiry_dt' string to a datetime object
        expiry_dt = datetime.strptime(data['expiry_dt'], '%a, %d %b %Y %H:%M:%S %Z')  # Adjust the format as needed

        # Create a new role record
        new_role = Role(
            role_id=None,
            role_listing_ver = 0,
            role_name=data['role_name'],
            job_type=data['job_type'],
            department=data['department'],
            job_description=data['job_description'],
            original_creation_dt=datetime.now(),
            expiry_dt=expiry_dt,
            hiring_manager_id=data['hiring_manager_id'],
            upd_hiring_manager_id=data['hiring_manager_id'],
            upd_dt=datetime.now(),
            active_status=1
        )
        
        # Create a list to store the RoleSkill records
        role_skills = []

        # Add the new role to the session
        db.session.add(new_role)
        db.session.commit()

        db.session.refresh(new_role)

        # Create a list to store the RoleSkill records
        role_skills = []

        # Loop through the list of skills and create RoleSkill records
        for skill_name in data['role_listing_skills']:
            role_listing_skills = RoleListingSkills(
                role_id=new_role.role_id,
                role_listing_ver=0,
                skills=skill_name[0],
                skills_proficiency=skill_name[1]
            )
            role_skills.append(role_listing_skills)

        # Add the RoleSkill records to the session
        db.session.add_all(role_skills)
  
        # Commit the session to persist the record in the database
        db.session.commit()

        response_data = {
            "role": new_role.json(),
            "role_listing_skills": [role_skill.json() for role_skill in role_skills]
        }

        return jsonify(response_data), 201
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        return f"Error inserting data: {str(e)}", 500
    
@role_routes.route('/API/v1/updateRole', methods=['POST'])
def updateRole():
    flag = 0
    try:
        data = request.get_json()

        # Convert the 'expiry_dt' string to a datetime object
        expiry_dt = datetime.strptime(data['expiry_dt'], '%a, %d %b %Y %H:%M:%S %Z')  # Adjust the format as needed
        orig_create_dt = datetime.strptime(data['orig_role_listing']['original_creation_dt'], '%a, %d %b %Y %H:%M:%S %Z')  # Adjust the format as needed

        flag += 1

        update_role = Role(
            role_id=data['orig_role_listing']['role_id'],
            role_listing_ver = int(data['orig_role_listing']['role_listing_ver']) + 1,
            role_name=data['role_name'],
            job_type=data['job_type'],
            department=data['department'],
            job_description=data['job_description'],
            original_creation_dt= orig_create_dt,
            expiry_dt=expiry_dt,
            hiring_manager_id=data['orig_role_listing']['hiring_manager_id'],
            upd_hiring_manager_id=data['hiring_manager_id'],
            upd_dt=datetime.now(),
            active_status=data['active_status']
        )

        role_skills = []

        # Loop through the list of skills and create RoleSkill records
        for skill_name in data['role_listing_skills']:
            role_listing_skills = RoleListingSkills(
                role_id=data['orig_role_listing']['role_id'],
                role_listing_ver=int(data['orig_role_listing']['role_listing_ver']) + 1,
                skills=skill_name[0],
                skills_proficiency=skill_name[1]
            )
            role_skills.append(role_listing_skills)

        flag += 1
        # Add the new role and role_skills to the session
        db.session.add(update_role)
        db.session.add_all(role_skills)

        # Commit the session to persist the record in the database
        db.session.commit()

        flag += 1
        processed_role = update_role.json()

        processed_role['role_listing_skills'] = []
        for role_skill in role_skills:
            processed_role['role_listing_skills'] += [role_skill.json()]

        return jsonify(processed_role), 200
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        if flag == 1:
            return f"Passed JSON data invalid or missing values, error: {str(e)}", 500
        elif flag ==2:
            return f"Error inserting data to database, possible issue with role record: {str(e)}", 500

        return f"Error inserting data: {str(e)}", 500

@role_routes.route('/API/v1/hideRole/<string:inputRoleId>')
def hideRole(inputRoleId):
    try:

        subquery = db.session.query(Role.role_id, db.func.max(Role.role_listing_ver).label('max_ver')).group_by(Role.role_id).subquery()
        query = db.session.query(Role).join(subquery, db.and_(Role.role_id == subquery.c.role_id, Role.role_listing_ver == subquery.c.max_ver))
        role = query.filter_by(role_id=inputRoleId).all().copy()[0]

        if role.active_status == 1:
            new_role = Role(
                role_id=role.role_id,
                role_listing_ver = role.role_listing_ver + 1,
                role_name=role.role_name,
                job_type=role.job_type,
                department=role.department,
                job_description=role.job_description,
                original_creation_dt= role.original_creation_dt,
                expiry_dt=role.expiry_dt,
                hiring_manager_id=role.hiring_manager_id,
                upd_hiring_manager_id=role.upd_hiring_manager_id,
                upd_dt=datetime.now(),
                active_status=0
            )

            subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
            query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
            skills = query.filter_by(role_id=inputRoleId).all().copy()
            new_skills = []
            for skill in skills:
                new_skills += [RoleListingSkills(
                    role_id=skill.role_id,
                    role_listing_ver=skill.role_listing_ver + 1,
                    skills=skill.skills,
                    skills_proficiency=skill.skills_proficiency
                )]

            # Add the new role and role_skills to the session
            db.session.add(new_role)
            db.session.add_all(new_skills)

            # Commit the session to persist the record in the database
            db.session.commit()

            processed_role = new_role.json()

            processed_role['role_listing_skills'] = []
            for role_skill in new_skills:
                processed_role['role_listing_skills'] += [role_skill.json()]

            return jsonify(processed_role), 200
        else:
            db.session.rollback()  # Rollback the session in case of an error
            return f"Error updating active_status, role already hidden", 500

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error

        return f"Error inserting data: {str(e)}", 500

@role_routes.route('/API/v1/unhideRole/<string:inputRoleId>')
def unhideRole(inputRoleId):
    try:

        subquery = db.session.query(Role.role_id, db.func.max(Role.role_listing_ver).label('max_ver')).group_by(Role.role_id).subquery()
        query = db.session.query(Role).join(subquery, db.and_(Role.role_id == subquery.c.role_id, Role.role_listing_ver == subquery.c.max_ver))
        role = query.filter_by(role_id=inputRoleId).all().copy()[0]

        if role.active_status == 0:
            new_role = Role(
                role_id=role.role_id,
                role_listing_ver = role.role_listing_ver + 1,
                role_name=role.role_name,
                job_type=role.job_type,
                department=role.department,
                job_description=role.job_description,
                original_creation_dt= role.original_creation_dt,
                expiry_dt=role.expiry_dt,
                hiring_manager_id=role.hiring_manager_id,
                upd_hiring_manager_id=role.upd_hiring_manager_id,
                upd_dt=datetime.now(),
                active_status=1
            )

            subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
            query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
            skills = query.filter_by(role_id=inputRoleId).all().copy()
            new_skills = []
            for skill in skills:
                new_skills += [RoleListingSkills(
                    role_id=skill.role_id,
                    role_listing_ver=skill.role_listing_ver + 1,
                    skills=skill.skills,
                    skills_proficiency=skill.skills_proficiency
                )]

            # Add the new role and role_skills to the session
            db.session.add(new_role)
            db.session.add_all(new_skills)

            # Commit the session to persist the record in the database
            db.session.commit()

            processed_role = new_role.json()

            processed_role['role_listing_skills'] = []
            for role_skill in new_skills:
                processed_role['role_listing_skills'] += [role_skill.json()]

            return jsonify(processed_role), 200
        else:
            db.session.rollback()  # Rollback the session in case of an error
            return f"Error updating active_status, role already active", 500

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error

        return f"Error inserting data: {str(e)}", 500

@role_routes.route('/API/v1/getSkills')
def getSkills():
    try:
        skills = db.session.query(RoleSkill.skill_name).distinct().all()
        skills = [skill[0] for skill in skills]
        return jsonify(skills), 200
    except Exception as e:

        return f"Error inserting data: {str(e)}", 500

