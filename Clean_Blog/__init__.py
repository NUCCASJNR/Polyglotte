#!/usr/bin/python3
"""Initializes app_view object"""
from flask import Blueprint, Flask, render_template, request, url_for, redirect
# from Clean_Blog.forms import SignupForm, LoginForm
from flask_bcrypt import Bcrypt
from models.engine.storage import Storage

storage = Storage()
storage.reload()

app = Flask(__name__)
app_views = Blueprint('app_views', __name__, url_prefix='/')


app.config['SECRET_KEY'] = '178d94e6aedab98a3349aeb7cb37713a'
bcrypt = Bcrypt(app)


from Clean_Blog.api import comments, following, followers, posts, states, users
from Clean_Blog import routes