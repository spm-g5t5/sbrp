from flask import jsonify, Blueprint, current_app, request
from models import Staff, StaffAccess, StaffSkill, RoleSkill
from models import db
import pandas as pd

database_routes = Blueprint('database_routes', __name__)

@database_routes.route('/API/v1/admin/cron/dbsyncall')
def dbSyncAll():

    #staff table from HRMS
    data_df = pd.read_csv('database/staff.csv')
    remap = {}

    model = ["staff_id", "staff_fname", "staff_lname", "dept", "country", "email"]
    for idx in range(0, len(data_df.keys())):
        remap[data_df.keys()[idx]] = model[idx]
    data_df = data_df.rename(columns=remap)
    for index, row in data_df.iterrows():
        # Use the primary key (id) or a unique constraint to identify existing records
        existing_record = Staff.query.filter_by(staff_id=row['staff_id']).first()
        
        if existing_record:
            # If the record exists, update its attributes
            existing_record.staff_fname = row['staff_fname']
            existing_record.staff_lname = row['staff_lname']
            existing_record.dept = row['dept']
            existing_record.country = row['country']
            existing_record.email = row['email']
        else:
            # If the record does not exist, create a new one
            new_entry = Staff(staff_id=row['staff_id'], staff_fname=row['staff_fname'], staff_lname=row['staff_lname'], dept=row['dept'], country=row['country'], email=row['email'])
            db.session.add(new_entry)

    #staff access table from LMS
    data_df = pd.read_csv('database/staff_access.csv')
    remap = {}

    model = ["staff_id", "access_rights"]
    for idx in range(0, len(data_df.keys())):
        remap[data_df.keys()[idx]] = model[idx]
    data_df = data_df.rename(columns=remap)
    for index, row in data_df.iterrows():
        # Use the primary key (id) or a unique constraint to identify existing records
        existing_record = StaffAccess.query.filter_by(staff_id=row['staff_id']).first()
        
        if existing_record:
            # If the record exists, update its attributes
            existing_record.access_rights = row['access_rights']
        else:
            # If the record does not exist, create a new one
            new_entry = StaffAccess(staff_id=row['staff_id'], access_rights=row['access_rights'])
            db.session.add(new_entry)

    #staff skill table from LMS
    data_df = pd.read_csv('database/staff_skill.csv')
    remap = {}

    model = ["staff_id", "skill_name"]
    for idx in range(0, len(data_df.keys())):
        remap[data_df.keys()[idx]] = model[idx]
    data_df = data_df.rename(columns=remap)
    for index, row in data_df.iterrows():
        # Use the primary key (id) or a unique constraint to identify existing records
        existing_record = StaffSkill.query.filter_by(staff_id=row['staff_id']).first()
        
        if existing_record:
            # If the record exists, update its attributes
            existing_record.access_rights = row['skill_name']
        else:
            # If the record does not exist, create a new one
            new_entry = StaffSkill(staff_id=row['staff_id'], skill_name=row['skill_name'])
            db.session.add(new_entry)


    #role skill table from LJPS
    data_df = pd.read_csv('database/role_skill.csv')
    remap = {}

    model = ["role_name", "skill_name"]
    for idx in range(0, len(data_df.keys())):
        remap[data_df.keys()[idx]] = model[idx]
    data_df = data_df.rename(columns=remap)
    for index, row in data_df.iterrows():
        # Use the primary key (id) or a unique constraint to identify existing records
        existing_record = RoleSkill.query.filter_by(role_name=row['role_name']).first()
        
        if existing_record:
            # If the record exists, update its attributes
            existing_record.access_rights = row['skill_name']
        else:
            # If the record does not exist, create a new one
            new_entry = RoleSkill(role_name=row['role_name'], skill_name=row['skill_name'])
            db.session.add(new_entry)


    db.session.commit()
    
    #TODO: add all other tables
    return "Data successfully updated / created", 200 