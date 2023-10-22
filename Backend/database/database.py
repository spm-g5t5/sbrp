from flask import jsonify, Blueprint, current_app, request
from models import Staff
from models import db
import pandas as pd

database_routes = Blueprint('database_routes', __name__)

@database_routes.route('/API/v1/admin/cron/dbsyncall')
def dbSyncAll():
    data_df = pd.read_csv('database/staff.csv')
    remap = {}
    staff_model = ["staff_id", "staff_fname", "staff_lname", "dept", "country", "email"]
    for idx in range(0, len(data_df.keys())):
        remap[data_df.keys()[idx]] = staff_model[idx]
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
            print('updated')
        else:
            # If the record does not exist, create a new one
            print("import")
            new_entry = Staff(staff_id=row['staff_id'], staff_fname=row['staff_fname'], staff_lname=row['staff_lname'], dept=row['dept'], country=row['country'], email=row['email'])
            db.session.add(new_entry)
    
    db.session.commit()
    
    #TODO: add all other tables
    return "Data successfully updated / created", 200 #TODO: add precise rows updated and imported