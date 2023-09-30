from flask import jsonify, Blueprint, current_app
from models import Role, RoleSkill

role_routes = Blueprint('role_routes', __name__)

#get all roles
@role_routes.route('/api/v1/viewRoles')
def viewRoles():
    roles = Role.query.all()
    return jsonify([role.json() for role in roles])

#get skills needed for a specific role
@role_routes.route('/api/v1/viewRoles/skill/<string:name>')
def getSkillsByRoleName(name):
    role_name = RoleSkill.query.filter_by(role_name=name)
    return jsonify([role.json() for role in role_name])