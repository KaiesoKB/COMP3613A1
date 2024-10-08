from App.database import db
from .user import User

class Student_reviews(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), nullable = False)
    staff_id = db.Column(db.Integer, db.ForeignKey(Staff.staff_id), nullable = False)
    review_description = db.Column(db.String(255), nullable = False)
    rating = db.Column(db.Integer, nullable = False)

    def __init__(self, student_id, staff_id, review_description, rating):
        self.student_id = student_id
        self.staff_id = staff_id
        self.review_description = review_description
        self.rating = rating
    
    def validate_rating(self, key, rating):
        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        return rating

    def get_json(self):
        return {
            'id': self.id,
            'staff_id': self.staff_id,
            'review_description': self.review_description,
            'rating': self.rating
        }
