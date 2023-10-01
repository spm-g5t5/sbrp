from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests
from models import Staff, StaffAccess

staff_routes = Blueprint('staff_routes', __name__)

#flask route post request template
@staff_routes.route('/API/v1/login', methods=['POST'])
def authStaff():
    if "User" in request.headers:
        try:
            user = request.headers.get("user")

            useraccess_records = StaffAccess.query.filter_by(email=user).all()
            if len(useraccess_records) == 1:
                return jsonify({
                    "login_status": 1,
                    "staff": useraccess_records[0].getStaffRole(),
                }), 200
            else:
                user_records = Staff.query.filter_by(email=user).all()
                if len(user_records) == 1:
                    return jsonify({
                        "login_status": -1,
                        "staff": user_records[0].verifyStaffExists(),
                        "error": "User has no access rights",
                    }), 200

                return jsonify({
                     "login_status": 0,
                    "error": "Invalid user"
                }), 400
            
        except:
            return jsonify({
                "error": "An error occured"
            }), 400
    return jsonify({
                "error": "User not in header"
            }), 500
    request.status_code = 500