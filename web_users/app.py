#!/usr/bin/python3
from os import getenv

from flask import Flask, jsonify, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import storage
from models.user import User

BLOG_MYSQL_USER = getenv("BLOG_MYSQL_USER")
BLOG_MYSQL_PWD = getenv("BLOG_MYSQL_PWD")
BLOG_MYSQL_HOST = getenv("BLOG_MYSQL_HOST")
BLOG_MYSQL_DB = getenv("BLOG_MYSQL_DB")
BLOG_ENV = getenv("BLOG_ENV")
app = Flask(__name__)

# Configure your database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{BLOG_MYSQL_USER}:{BLOG_MYSQL_PWD}@{BLOG_MYSQL_HOST}:3306/{BLOG_MYSQL_DB}'
db = SQLAlchemy(app)

@app.teardown_appcontext
def close_db_connection(exception):
    """
    calls storage.close() to close the database connection
    """

    storage.close()


# @app.errorhandler(404)
# def error(error):
#     """
#     Handles 404 error
#     """
#     return make_response(jsonify({"error": "Not found"}), 404)

from web_users.views import *

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
