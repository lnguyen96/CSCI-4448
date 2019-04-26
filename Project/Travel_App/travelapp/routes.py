from flask import render_template, url_for, flash, redirect, request
from travelapp import app, db, bcrypt
from travelapp.forms import RegistrationForm, LoginForm, Destination
from flask_login import login_user, current_user, logout_user, login_required
from travelapp.models import User, Car, Routes
from travelapp.distanceAPI import getDistance

@app.route("/")
@app.route("/home")
def home():
    posts = Routes.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


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


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


@app.route("/route/new", methods=['GET', 'POST'])
@login_required
def new_route():
    form = Destination()
    if form.validate_on_submit():
        loc = Routes(start=form.start.data, end=form.end.data, make=form.make.data, model=form.model.data, year=form.year.data, dist=getDistance(form.start.data, form.end.data))
        db.session.add(loc)
        db.session.commit()
        flash("Location has been entered", "success")
        return redirect(url_for("home"))
    return render_template('travel.html', title='Travel', form=form)

@app.route("/route/<int:route_id>")
def routed(route_id):
    route = Routes.query.get_or_404(route_id)
    return render_template("specificroute.html", route=route)


@app.route("/route/<int:route_id>/delete")
@login_required
def delete_route(route_id):
    route = Routes.query.get_or_404(route_id)
    db.session.delete(route)
    db.session.commit()
    flash("Your route has been deleted", 'success')
    return redirect(url_for("home"))
