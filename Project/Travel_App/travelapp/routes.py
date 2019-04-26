'''
File used to send data to corresponding HTML page
Query data here to use for calculation or send to be displayed
'''

from flask import render_template, url_for, flash, redirect, request
from travelapp import app, db, bcrypt
from travelapp.forms import RegistrationForm, LoginForm, Destination
from flask_login import login_user, current_user, logout_user, login_required
from travelapp.models import User, Car, Routes, Gas
from travelapp.distanceAPI import getDistance
from travelapp.distanceAPI import calculateCost

# Queries all routes in a table for a user and displays on our home page
@app.route("/")
@app.route("/home")
def home():
    posts = Routes.query.all()
    return render_template('home.html', posts=posts)

# Displays information about group members and some instructions on how to use app
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Renders the register page, takes in user specified data and sends elsewhere to be validated and then adds to database depending on validation
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Renders page for existing users to login, similar to above takes user info and if validated redirects to home page with user logged in
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Renders login page when logged in user logs out
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# Pretty empty right now, only displays name of user logged in, we used it mainly to verify logging in works
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

# Main route that handles majority of our app functionality
@app.route("/route/new", methods=['GET', 'POST'])
@login_required
def new_route():
    form = Destination()
    if form.validate_on_submit():
        # Queries database for necessary information after user input 
        car = Car.query.filter_by(make=form.make.data, model=form.model.data, year=form.year.data).first()
        milesPer = car.MPG
        fuelType = car.gas
        fuelType = fuelType.split()[0]
        pricePer = Gas.query.filter_by(name=fuelType).first()
        pricePer = pricePer.cost
        # Using queried information and sending it to distanceAPI.py to perform calculations
        distance = getDistance(form.start.data, form.end.data)
        # Creating an entry in database to be displayed with all info for a specific route
        loc = Routes(start=form.start.data, end=form.end.data, make=form.make.data, model=form.model.data, year=form.year.data, dist=distance, cost=calculateCost(distance, pricePer, milesPer))
        db.session.add(loc)
        db.session.commit()
        flash("Location has been entered", "success")
        return redirect(url_for("home"))
    return render_template('travel.html', title='Travel', form=form)

# Displays information for a specific route, essentially acts as a more info page
@app.route("/route/<int:route_id>")
def routed(route_id):
    route = Routes.query.get_or_404(route_id)
    return render_template("specificroute.html", route=route)

# Confirmation page for when user decides to delete an existing route
@app.route("/route/<int:route_id>/delete")
@login_required
def delete_route(route_id):
    route = Routes.query.get_or_404(route_id)
    db.session.delete(route)
    db.session.commit()
    flash("Your route has been deleted", 'success')
    return redirect(url_for("home"))
