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
    follower_id = follower_data.get("followed_user_id")
    follower = storage.get(Follower, follower_id)
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
    
    abort(404)

@app_views.route("/users/<user_id>/unfollow", methods=["POST"],
                 strict_slashes=False)
def unfollow(user_id):
    """
    unfollows a user as a follower to a user
    """
    follower_data = request.get_json()
    follower_id = follower_data.get("followed_user_id")
    follower = storage.get(Follower, follower_id)
    print(follower)
    if not follower:
        new_user = storage.get(User, user_id)
        print(new_user)
        if not follower_data:
            return jsonify({"error": "Not a JSON"})
        if follower_id  == user_id:
            return jsonify({"error": "Cannot unfollow yourself"})
        follow = Follower()
        for key, value in follower_data.items():
            setattr(follow, key, value)
        new_user.decrement_followers_count()
        follow.save()
        return jsonify(follow.to_dict()), 201
    abort(404)


@app_views.route("/users/<user_id>/followers", methods=["GET"],
                 strict_slashes=False)
def get_followers(user_id):
    """
    Gets followers of a User
    """
    user = storage.get(User, user_id)
    follow_list = []
    if user:
        for follower in storage.all(Follower).values():
            if follower.followed_user_id == user_id:
                follow_list.append(follower.to_dict())
        return jsonify(follow_list)
    abort(404)
