#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """
    Docs later
    """

    users_list = []
    users = storage.all(User)
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route("/users/<user_id>", methods=["GET"], strict_slashes=False)
def get_user_using_userid(user_id):
    """
    Gets user uring the user_id
    """
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404)


@app_views.route("/users", methods=["POST"], strict_slashes=False)
def post_user():
    """
    Docs later trying to test
    """

    user_data = request.get_json()
    user = User()
    for key, value in user_data.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 201
