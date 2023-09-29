from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests
from models import Staff, StaffAccess

staff_routes = Blueprint('staff_routes', __name__)

# for apply
@staff_routes.route('/viewStaffAccess')
def viewStaffAccess():
    staffaccess_lst = StaffAccess.query.all()
    json = jsonify([staff.json() for staff in staffaccess_lst])
    return json


#flask route post request template
@staff_routes.route('/login', methods=['POST'])
def authStaff():
    if "User" in request.headers:
        try:
            user = request.headers.get("user")

            useraccess_records = StaffAccess.query.filter_by(email=user).all()
            if len(useraccess_records) == 1:
                return jsonify({
                    "login_status": 1,
                    "staff": useraccess_records[0].getStaffRole(),
                    "message": "User login successful",

                }), 200
            else:
                user_records = Staff.query.filter_by(email=user).all()
                if len(user_records) == 1:
                    return jsonify({
                        "login_status": -1,
                        "staff": user_records[0].verifyStaffExists(),
                        "message": "User has no access rights",

                    }), 200

                return jsonify({
                     "login_status": 0,
                    "message": "Invalid user"
                }), 400
            
        except:
            return jsonify({
                "message": "An error occured"
            }), 400
    return jsonify("User not in header"), 500
    