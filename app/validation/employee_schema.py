from marshmallow import Schema, fields


class EmployeeCreateSchema(Schema):
  first_name = fields.String(required=True)
  last_name = fields.String()
  email = fields.String(required=True)
  phone_number = fields.String(required=True)
  position = fields.String(required=True)
  age = fields.Int(required=True)
  birthdate = fields.Date(required=True)

class EmployeeUpdateSchema(Schema):
  first_name = fields.String()
  last_name = fields.String()
  email = fields.String()
  phone_number = fields.String()
  position = fields.String()
  age = fields.Int()
  birthdate = fields.Date()
