from App.database import db

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.string(30), nullable = False)
    reviews = db.relationship('Review', backred = 'student')

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_json(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            review_list = []
            for review in self.reviews:
                reviews_list.append(review.get_json())
            'reviews': reviews_list
        }
