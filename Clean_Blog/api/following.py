#!/usr/bin/python3
"""
HAndles all RESTFUL APIs for following
"""

from flask import abort, jsonify, request

from Clean_Blog import app_views
from models import storage
from models.following import Following
from models.user import User


@app_views.route("/users/<user_id>/following", methods=["POST"],
                 strict_slashes=False)
def following(user_id):
    """
    Adds a user as a follower to a user
    """
    follower_data = request.get_json()
    following_id = follower_data.get("follower_user_id")
    following = storage.get(Following, following_id)
    if not following:
        new_user = storage.get(User, user_id)
        print(new_user)
        if not follower_data:
            return jsonify({"error": "Not a JSON"})
        if following_id  == user_id:
            return jsonify({"error": "Cannot follow yourself"})
        follow = Following()
        for key, value in follower_data.items():
            setattr(follow, key, value)
        new_user.increment_following_count()
        follow.save()
        return jsonify(follow.to_dict()), 201
    
    abort(404)