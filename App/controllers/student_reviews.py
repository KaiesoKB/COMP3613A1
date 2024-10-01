from App.models import Student_reviews
from App.database import db

def add_review(student_id, review_description, rating):
  if not Student.query.get(student_id):
    return {"message": "student does not exist"}

  new_review = Review(student_id = student_id, staff_id = staff_id, review_description = review_description, rating = rating)
  db.session.add(new_review)
  db.session.commit()
  return {"message": "review has been added"}

def view_student_reviews(student_id):
  if not Student.query.get(student_id):
    return {"message": "student does not exist"}

  if not Student_reviews.query.filter_by(student_id = student_id).all():
    return {"message": "This student has no reviews"}

  review_list = []
  for review in reviews:
      review_list.append(review.get_json())
  return {"reviews": review_list}
