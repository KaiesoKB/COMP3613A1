from App.models import Student
from App.database import db

def add_student(student_id, student_name):
  if Student.query.filter_by(student_id=student_id).first():
    return {"message": "Student already exists."}

  new_student = Student(student_id = student_id, name = student_name)
  db.session.add(new_student)
  db.session.commit()
  return {"message": f"student {student_name} has been added."}

def search_student(student_id):
  if Student.query.filter_by(student_id=student_id).first():
    return student.get_json()
  else:
    return {"message": "Could not find student"}

    
