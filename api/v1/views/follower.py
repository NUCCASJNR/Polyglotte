#!/usr/bin/python3
"""
HAndles all RESTFUL APIs for followers
"""

from flask import abort, jsonify, request

from api.v1.views import app_views
from models import storage
from models.follower import Follower
from models.user import User


@app_views.route("/users/<user_id>/follow/<follower_id>", methods=["POST"],
                 strict_slashes=False)
def post_new_follower(user_id, follower_id):
    """
    Adds a user as a follower to a user
    """
    follower_data = request.get_json()
    # follower_id = follower_data.get("followed_user_id")
    follower = storage.get(Follower, "follower_id")
    print(follower)
    if not follower:
        new_user = storage.get(User, user_id)
        print(new_user)
        if not follower_data:
            return jsonify({"error": "Not a JSON"})
        if follower_id  == user_id:
            return jsonify({"error": "Cannot follow yourself"})
        follow = Follower()
        for key, value in follower_data.items():
            setattr(follow, key, value)
        new_user.increment_followers_count()
        follow.save()
        return jsonify(follow.to_dict()), 201
    
    