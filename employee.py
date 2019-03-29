from flask import Flask, jsonify, request
from app import app, db
from model import Employee


@app.route('/employee')
def tesUser():
    return 'tes koneksi employee'
# ================================== ADD EMPLOYEE ==================================

@app.route('/addEmployee', methods=["POST"])
def add_employee():

    body = request.json

    password = body['password']
    email = body['email']
    fullname = body['fullname']
    position = body['position']

    try:
        employee = Employee(
            password=password,
            email=email,
            fullname=fullname,
            position=position
        )

        db.session.add(employee)
        db.session.commit()
        return "add employee. employee id={}".format(employee.employee_id), 200

    except Exception as e:
        return(str(e)), 400

# ========================== GET ALL EMPLOYEE =============================================
@app.route('/getAllEmployee', methods=["GET"])
def get_all_employee():
        try:
                employee = Employee.query.order_by(Employee.employee_id).all()
                return jsonify([usr.serialize()
                for usr in employee])
        except Exception as e:
                return (str(e))

# ============================= GET EMPLOYEE BY ID ==========================================
@app.route('/getEmployeeBy/<employeeId_>', methods=["GET"])
def get_employee_by(employeeId_):
        try:
                employe = Employee.query.filter_by(employee_id=employeeId_).first()
                return jsonify(employe.serialize())
        except Exception as e:  
                return (str(e))

# ================================= LOG IN =====================================================
@app.route('/login', methods=['POST'])
def login():
    response = {}
    body = request.json
    email = body['email']
    password = body['password']
    isLogin = False

    try:
        employers = get_all_employee().json
        for employee in employers:
            if email == employee['email']:
                if password == employee['password']:
                    isLogin = True

    except Exception as e:
        response['Error'] = str(e)
        # return str(e)

    if isLogin:
        response['message'] = 'Login success, welcome {}'.format(email)
        code = 200
    else:
        response['message'] = 'Login failed, username or password is wrong'
        code = 400
    return jsonify(response), code
