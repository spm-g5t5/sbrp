from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests

staff_routes = Blueprint('staff_routes', __name__)

# for apply
@staff_routes.route('/viewStaff')
def viewApplicants():
    return 'staffs'

# for config testing
@staff_routes.route('/test/configtest')
def testConfigTest():
    return current_app.config["DB_HOST"] 