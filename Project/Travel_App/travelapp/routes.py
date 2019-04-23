from flask import render_template, url_for, flash, redirect
from travelapp import app, db, bcrypt
from travelapp.forms import registerform, loginform
from travelapp.models import User, Post
from flask_login import login_user, current_user, logout_user

posts = [
    {
        'author': 'NULL',
        'title': 'NULL',
        'content': 'NULL',
        'date': 'NULL'
    },
    {
        'author': 'NULL2',
        'title': 'NULL2',
        'content': 'NULL2',
        'date': 'NULL2'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods = ["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = registerform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created!", "success")
        return redirect(url_for("login"))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remembered.data)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Check Email or Password", "danger")
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))