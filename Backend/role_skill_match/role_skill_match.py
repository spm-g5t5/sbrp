from flask import jsonify, Blueprint, current_app, request
from models import RoleListingSkills, StaffSkill
from models import db

rs_match_routes = Blueprint('rs_match_routes', __name__)

@rs_match_routes.route('/API/v1/getRoleSkillMatch', methods=['POST'])
def getSkillsByRoleName():
    try:
        data = request.get_json()

        input_staff_id = data['staff_id']
        input_role_id = data['role_id']
        
        # Query staff skills
        staff_skills = StaffSkill.query.filter(StaffSkill.staff_id == input_staff_id).all()

        # Query role skills
        subquery = db.session.query(RoleListingSkills.role_id, db.func.max(RoleListingSkills.role_listing_ver).label('max_ver')).group_by(RoleListingSkills.role_id).subquery()
        query = db.session.query(RoleListingSkills).join(subquery, db.and_(RoleListingSkills.role_id == subquery.c.role_id, RoleListingSkills.role_listing_ver == subquery.c.max_ver))
        role_skills = query.filter_by(role_id=input_role_id).all()

        # Reformat objects into lists
        staff_skills_list = [skill.json()['skill_name'] for skill in staff_skills]
        role_skills_list = [role.json()['skill_name'] for role in role_skills]
        total_role_skills = len(role_skills_list)


        staff_dict = {item: 0 for item in staff_skills_list}
        role_dict = {item: 0 for item in role_skills_list}
        # compare skill match
        for skill in role_skills_list:
            if skill in staff_skills_list:
                staff_dict[skill] = 1
                role_dict[skill] = 1
        
        # calculate skill match percentage
        skill_match_pct = int(sum(staff_dict.values()) / total_role_skills * 100)

        #list of skills that staff and role has
        skill_match_list = [skill for skill in staff_skills_list if skill in role_skills_list]

        # list of skills that staff has but role does not
        staff_skills_not_in_role = []

        for skill, value in staff_dict.items():
            if value == 0:
                staff_skills_not_in_role.append(skill)

        #list of skills that role has but staff does not
        role_skills_not_in_staff = []

        for skill, value in role_dict.items():
            if value == 0:
                role_skills_not_in_staff.append(skill)

        output = {
            'skill_match_pct': skill_match_pct,
            'skill_match': skill_match_list,
            'staff_skills_unmatch': staff_skills_not_in_role,
            'role_skills_unmatch': role_skills_not_in_staff
        }

        # Return a JSON response with the list of skills for the specified role name
        return jsonify(output), 200
    except Exception as e:
        # Handle other exceptions (e.g., database errors) with a 500 Internal Server Error
        return jsonify({"error": str(e)}), 500