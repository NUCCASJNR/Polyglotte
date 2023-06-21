#!/usr/bin/python3
"""
HAndles all RESTFUL APIs for followers
"""

from flask import abort, jsonify, request

from api.v1.views import app_views
from models import storage
from models.follower import Follower
from models.user import User


@app_views.route("/users/<user_id>/follow", methods=["POST"],
                 strict_slashes=False)
def post_new_follower(user_id):
    """
    Adds a user as a follower to a user
    """
    follower_data = request.get_json()
    new_user = storage.get(User, user_id) # Get the existing user object
    if not follower_data:
        return jsonify({"error": "Not a JSON"})
    if new_user == follower_data.get("user_id"):
        return jsonify({"error": "Cannot follow yourself"})
    follow = Follower()
    for key, value in follower_data.items():
        setattr(follow, key, value)
    new_user.increment_followers_count()
    follow.save()
    return jsonify(follow.to_dict()), 201
    