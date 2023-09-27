from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests

# from .apply import models
# from .role import models
# from .staff import models

routes = Blueprint('routes', __name__)

@routes.route('/')
def hello_world():
    return 'Hello SPM!'

# for staff
@routes.route('/viewRoleListing')
def viewRoleListing():
    return 'View Role Listing'

# for admin
@routes.route('/viewApplicants')
def viewApplicants():
    return 'View Applicants'

# for config testing
@routes.route('/test/configtest')
def testConfigTest():
    return current_app.config["DB_HOST"] 