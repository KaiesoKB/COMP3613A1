

def add_review(student_id, staff_id, review_description, rating):
  if not Student.query.get(student_id):
    return {"message": "student does not exist"}

  new_review = Review(student_id = student_id, staff_id = staff_id, review_description = review_description, rating = rating)
  db.session.add(new_review)
  db.session.commit()
  return {"message": "review has been added"}
