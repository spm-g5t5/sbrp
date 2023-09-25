from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello SPM!'

# for staff
@app.route('/viewRoleListing')
def viewRoleListing():
    return 'View Role Listing'

# for admin
@app.route('/viewApplicants')
def viewApplicants():
    return 'View Applicants'