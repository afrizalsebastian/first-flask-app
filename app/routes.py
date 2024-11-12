from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app import db
from app.dto.EmployeeDto import EmployeeDto
from app.models import Employee
from app.validation.employee_schema import (EmployeeCreateSchema,
                                            EmployeeUpdateSchema)

api = Blueprint('api', __name__, url_prefix='/api')

@api.route("/employees", methods=['GET'])
def get_all_employee():
  employees = Employee.query.all()
  json_employees = list(map(lambda employee: EmployeeDto.to_employe_dto(employee), employees))

  return jsonify({
    'status': 'success',
    'message': 'ok',
    'data': json_employees,
  }), 200

@api.route("/employees", methods=['POST'])
def create_employee():
  body = request.get_json()
  schema = EmployeeCreateSchema()
  try:
    body = schema.load(body)
  except ValidationError as err:
    return jsonify({
      'status': 'error',
      'message': f'bad request, {err.messages}'
    }), 400

  employee = EmployeeDto.from_createdto_to_employee(body)
  db.session.add(employee)
  db.session.commit()

  return jsonify({
    'status': 'success',
    'message': 'ok',
  }), 201

@api.route("/employees/<int:employee_id>", methods=['GET'])
def get_employee_by_id(employee_id):
  employee = Employee.query.get(employee_id)
  
  if not employee:
    return jsonify({
    'status': 'error',
    'message': f'employee with id {employee_id} not found',
  }), 404

  return jsonify({
    'status': 'success',
    'message': 'ok',
    'data': EmployeeDto.to_employee_detail_dto(employee),
  }), 200

@api.route("/employees/<int:employee_id>", methods=['PUT'])
def update_employee(employee_id):
  employee = Employee.query.get(employee_id)
  
  if not employee:
    return jsonify({
    'status': 'error',
    'message': f'employee with id {employee_id} not found',
  }), 404

  body = request.get_json()
  schema = EmployeeUpdateSchema()
  try:
    body = schema.load(body)
  except ValidationError as err:
    return jsonify({
      'status': 'error',
      'message': f'bad request, {err.messages}'
    }), 400
  
  employee.first_name = body.get('first_name', employee.first_name)
  employee.last_name = body.get('last_name', employee.last_name)
  employee.position = body.get('position', employee.position)
  employee.age = body.get('age', employee.age)
  employee.birthdate = body.get('birthdate', employee.birthdate)
  employee.email = body.get('email', employee.email)
  employee.phone_number = body.get('phone_number', employee.phone_number)
  db.session.commit()

  return jsonify({
    'status': 'success',
    'message': 'ok',
    'data': EmployeeDto.to_employee_detail_dto(employee),
  }), 200

@api.route("/employees/<int:employee_id>", methods=['DELETE'])
def delete_employee(employee_id):
  employee = Employee.query.get(employee_id)
  
  if not employee:
    return jsonify({
    'status': 'error',
    'message': f'employee with id {employee_id} not found',
  }), 404

  db.session.delete(employee)
  db.session.commit()

  return jsonify({
    'status': 'success',
    'message': 'employee deleted',
  }), 200


@api.route("/")
def base_route():
  return jsonify({
    'status': 'success',
    'message': 'api running',
  }), 200
