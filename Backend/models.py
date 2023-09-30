# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from extensions import db

class Apply(db.Model):
    __tablename__ = 'APPLICATION'
    application_id = db.Column(db.Integer, primary_key=True)
    applicant_staff_id = db.Column(db.Integer, nullable=False)
    applicant_existing_role = db.Column(db.String(50), nullable=False)
    applicant_existing_dept = db.Column(db.String(50), nullable=False)
    application_status = db.Column(db.String(20), nullable=False)
    date_applied = db.Column(db.DateTime, nullable=False)
    applied_role_id  = db.Column(db.Integer, nullable=False)

    def __init__(self, application_id, applicant_staff_id, applicant_existing_role, applicant_existing_dept, application_status, date_applied, applied_role_id):
        self.application_id = application_id
        self.applicant_staff_id = applicant_staff_id
        self.applicant_existing_role = applicant_existing_role
        self.applicant_existing_dept = applicant_existing_dept
        self.application_status = application_status
        self.date_applied = date_applied
        self.applied_role_id = applied_role_id

    def json(self):
        return {"application_id": self.application_id, "applicant_staff_id": self.applicant_staff_id, "applicant_existing_role": self.applicant_existing_role, "applicant_existing_dept": self.applicant_existing_dept, "application_status": self.application_status, "date_applied": self.date_applied, "applied_role_id": self.applied_role_id}
class Staff(db.Model):
    __tablename__ = 'STAFF'
    staff_id = db.Column(db.Integer, primary_key=True)
    staff_fname = db.Column(db.String(50), nullable=False)
    staff_lname = db.Column(db.String(50), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def verifyStaffExists(self):
        json = {
            "staff_id": self.staff_id,
        }

        return json
class StaffAccess(Staff):
    __tablename__ = 'STAFF_ACCESS'
    staff_id  = db.Column(db.Integer, db.ForeignKey("STAFF.staff_id"), primary_key=True)
    access_rights = db.Column(db.Integer, nullable=False)

    def getStaffRole(self):
        json = {
            "staff_id": self.staff_id,
            "access_rights": self.access_rights,
        }

        return json

