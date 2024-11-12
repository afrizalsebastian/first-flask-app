from app import db


class Employee(db.Model):
  __tablename__ = 'employees'
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=True)
  position = db.Column(db.String(50), nullable=True)
  age = db.Column(db.Integer, nullable=False)
  birthdate = db.Column(db.Date, nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  phone_number = db.Column(db.String(25), unique=True, nullable=False)

  def __init__(self, first_name, last_name, email, phone_number, position, age, birthdate):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.phone_number = phone_number
    self.position = position
    self.birthdate = birthdate
    self.age = age

  def __repr__(self) -> str:
    return '<Employee %r>' % f'{self.first_name} {self.last_name}'