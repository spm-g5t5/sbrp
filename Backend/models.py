# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()
from extensions import db

class Apply(db.Model):
    __tablename__ = 'application'
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

class ApplySkill(db.Model):
    __tablename__ = 'application_skills'
    application_id = db.Column(db.Integer, primary_key=True)
    applicant_skills = db.Column(db.String(50), nullable=False)

    def __init__(self, application_id, applicant_skills):
        self.application_id = application_id
        self.applicant_skills = applicant_skills

    def json(self):
        return {"application_id": self.application_id, "application_skills": self.applicant_skills}
    
class Role(db.Model):
    __tablename__ = 'role_listing'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    job_description = db.Column(db.String(50), nullable=False)
    original_creation_dt = db.Column(db.DateTime, nullable=False)
    expiry_dt = db.Column(db.DateTime, nullable=False)
    hiring_manager_id = db.Column(db.Integer, nullable=False)

    def __init__(self, role_id, role_name, job_type, department, job_description, original_creation_dt, expiry_dt, hiring_manager_id):
        self.role_id = role_id
        self.role_name = role_name
        self.job_type = job_type
        self.department = department
        self.job_description = job_description
        self.original_creation_dt = original_creation_dt
        self.expiry_dt = expiry_dt
        self.hiring_manager_id = hiring_manager_id

    def json(self):
        return {"role_id": self.role_id, "role_name": self.role_name, "job_type": self.job_type, "department": self.department, "job_description": self.job_description, "original_creation_dt": self.original_creation_dt, "expiry_dt": self.expiry_dt, "hiring_manager_id": self.hiring_manager_id}
    
class RoleSkill(db.Model):
    __tablename__ = 'role_skill'
    role_name = db.Column(db.String(20), primary_key=True)
    skill_name = db.Column(db.String(50), primary_key=True)

    def __init__(self, role_name, skill_name):
        self.role_name = role_name
        self.skill_name = skill_name

    def json(self):
        return {"role_name": self.role_name, "skill_name": self.skill_name}
    