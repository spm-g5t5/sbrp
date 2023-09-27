from flask import Flask, request, jsonify, Blueprint, render_template, current_app
import json
import requests

apply_routes = Blueprint('apply_routes', __name__)

# for admin
@apply_routes.route('/viewApplicants')
def viewApplicants():
    return 'View Applicants'

# for config testing
@apply_routes.route('/test/configtest')
def testConfigTest():
    return current_app.config["DB_HOST"] 