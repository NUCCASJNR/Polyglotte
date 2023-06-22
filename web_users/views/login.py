#!/usr/bin/python3

from os import getenv

from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

from models import storage
from models.user import User
from web_users.app import app


@app.route('/', methods=['GET'])
def index():
    return render_template('signup.html')
@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

# Define the route to handle the signup form submission
@app.route('/signup', methods=['POST'])
def signup():
    # Get the form data submitted by the user
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    existing_mail = storage.query(User, "email", email)
    existing_username = storage.query(User, "username", username)
    if not existing_mail and not existing_username:
        user_attr = {
            "username": username,
            "password": generate_password_hash(password),
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }
        new_user = User(**user_attr)
        new_user.save()
        flash('User created successfully!')
    else:
        flash('User already exists!')
    
    return redirect(url_for('login'))


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

# Define the route to handle the login form submission
@app.route('/login', methods=['POST'])
def login():
    # Get the form data submitted by the user
    username = request.form.get('username')
    password = request.form.get('password')
    user = storage.query(User, "username", username)
    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('welcome'))
    else:
        flash('Invalid username or password!')
        return redirect(url_for('login_page'))

@app.route('/login-success')
def login_success():
    return 'Login successful!'

@app.route('/welcome', methods=['GET'])
@login_required
def welcome():
    return render_template('welcome.html', username=current_user.username)