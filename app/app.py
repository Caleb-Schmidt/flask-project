from flask import Flask, render_template, request, flash, redirect
import requests
from .forms import *
from flask_login import current_user
from models import User
from . import create_app

app = create_app()

@app.route('/')
def homepage():
    return render_template("homepage.html.j2")

@app.route('/pokemon')
def pokemon():
    return render_template("pokemon.html.j2")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # LOGIN THE USER HERE
        email = form.email.data.lower()
        password = form.password.data

        if email in app.config.get('REGISTERED_USERS') and \
            password == app.config.get('REGISTERED_USERS').get(email).get('password'):
            #Login Success!!!
            return f"Login Success Welcome { app.config.get('REGISTERED_USERS').get(email).get('name') }"
        error_string = "Incorrect Email/Password Combo"
        return render_template('login.html.j2', loginerror=error_string, form=form)
    return render_template('login.html.j2', form=form)

@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        return "Welcome To our App... Thanks for registering"
    return render_template('register.html.j2', form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if request.method == 'POST' and form.validate_on_submit():
        edited_user_data = {
            "first_name": form.first_name.date.title(),
            "last_name": form.first_name.date.title(),
            "email": form.email.data.lower(),
            "password": form.password.data,
            "icon": form.icon.data
        }
        user = User.query.filter_by(email = edited_user_data['email'])
        if user and user.email != current_user.email:
            flash("Email is already in use", "danger")
            return redirect("/edit_profile")

        current_user.from_dict(edited_user_data)
        current_user.save()
        flash("Profile Updated", "success")
        return redirect("/")
    return render_template('register.html.j2', form=form)