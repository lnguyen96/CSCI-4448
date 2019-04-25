from travelapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cars = db.relationship('Car', backref='name', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    cylinder = db.Column(db.Integer, nullable=False)
    gas = db.Column(db.String(20), nullable=False)
    MPG = db.Column(db.Float, nullable=False)
    annualFuelCost = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"User('{self.make}', '{self.model}', '{self.year}')"

class Routes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(120), unique=True, nullable=False)
    end = db.Column(db.String(120), unique=True, nullable=False)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Routes('{self.start}', '{self.end}', '{self.make}', '{self.model}', '{self.year}')"
