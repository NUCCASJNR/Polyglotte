#!/usr/bin/python3

"""
Docs Soon
"""

from models import storage
from Clean_Blog import app_views
from flask import jsonify


@app_views.route("/blog_status", methods=["GET"], strict_slashes=False)
def display_status():
    """
    Docs soon
    """
    return jsonify({"status": "OK"})


@app_views.route("/classes_len", methods=["GET"], strict_slashes=False)
def show_len():
    """
    Docs soon
    """
    return jsonify({"users": storage.count("User")})
