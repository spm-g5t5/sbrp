from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests

role_routes = Blueprint('role_routes', __name__)

# for admin
@role_routes.route('/viewRoles')
def viewApplicants():
    return 'View Roles'

# for config testing
@role_routes.route('/test/configtest')
def testConfigTest():
    return current_app.config["DB_HOST"] 