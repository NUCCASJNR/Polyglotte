#!/usr/bin/python3

"""
Starts the Flask Application
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db_connection(exception):
    """
    calls storage.close() to close the database connection
    """

    storage.close()


@app.errorhandler(404)
def error(error):
    """
    Handles 404 error
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # host = getenv("BLOG_API_HOST")
    # port = getenv("BLOG_API_PORT")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
