from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

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

class Staff(db.Model):
    staff_id = db.Colmumn(db.Integer, primary key = True, unique = True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, staff_id, name):
        self.staff_id = staff.id
        self.name = name

    def get_json(self):
        return {
            'staff_id': self.staff_id,
            'name': self.name
        }

class Student_review(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), nullable = False)
    staff_id = db.Column(db.Integer, db.ForeignKey(Staff.staff_id), nullable = False)
    review_description = db.Column(db.String(255), nullable = False)
    rating = db.Column(db.Integer, nullable = False)

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

            
