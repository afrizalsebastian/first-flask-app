from app.models import Employee


class EmployeeDto():

  @staticmethod
  def to_employe_dto(employee: Employee):
    return {
      'id': employee.id,
      'first_name': employee.first_name,
      'last_name': employee.last_name,
      'position': employee.position,
    }
  
  @staticmethod
  def to_employee_detail_dto(employee: Employee):
    return {
      'id': employee.id,
      'first_name': employee.first_name,
      'last_name': employee.last_name,
      'position': employee.position,
      'age': employee.age,
      'birthdate': employee.birthdate,
      'email': employee.email,
      'phone_number': employee.phone_number,
    }
  
  @staticmethod
  def from_createdto_to_employee(employee_dto):
    return Employee(
        first_name=employee_dto['first_name'],
        last_name=employee_dto['last_name'] if employee_dto['last_name'] else '',
        position=employee_dto['position'],
        age=employee_dto['age'],
        birthdate=employee_dto['birthdate'],
        phone_number=employee_dto['phone_number'],
        email=employee_dto['email'],
      )