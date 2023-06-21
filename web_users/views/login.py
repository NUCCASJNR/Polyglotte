#!/usr/bin/python3

from web_users.app import app

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models.user import User 
from os import getenv
from models import storage



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
    # Create a new user object
    new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    new_user.save()
    # Add the user to the database session and commit the changes


    # Return a success message or redirect the user to a login page
    return 'Signup successful!'