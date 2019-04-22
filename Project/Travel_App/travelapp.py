from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@app.route("/")
def home():
    return render_template('travel.html')

@app.route("/login")
def login():
    return render_template('travel.html')

@app.route("/travel")
def travel():
    return render_template('travel.html')


if __name__ == '__main__':
    app.run(debug=True)