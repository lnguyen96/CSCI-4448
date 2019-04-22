from flask import render_template, url_for, flash, redirect
from travelapp import app
#from travelapp.forms import RegustrationForm, LoginForm
from travelapp.models import User, Car

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/travel")
def travel():
    return render_template('travel.html', title='Travel')
