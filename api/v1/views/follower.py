#!/usr/bin/python3
"""
HAndles all RESTFUL APIs for followers
"""

from flask import abort, jsonify, request

from api.v1.views import app_views
from models import storage
from models.follower import Follower
from models.user import User


# @app_views.route("/users/<user_id>/follow", methods=["POST"],
#                  strict_slashes=False)
# def post_new_follower