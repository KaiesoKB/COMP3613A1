from App.models import Student_reviews
from App.database import db

def view_student_reviews(student_id):
  if not Student.query.get(student_id):
    return {"message": "student does not exist"}

  student_reviews = Student_reviews.query.filter_by(student_id = student_id).all():
  if not student_reviews:
    return {"message": "This student has no reviews"}

  review_list = []
  for review in student_reviews:
      review_list.append(review.get_json())
  return {"reviews": review_list}
