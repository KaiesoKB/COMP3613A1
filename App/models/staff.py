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
