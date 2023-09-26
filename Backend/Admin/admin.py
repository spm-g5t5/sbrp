from app import app

@app.route('/viewApplicants')
def viewApplicants():
    return 'View Applicants'