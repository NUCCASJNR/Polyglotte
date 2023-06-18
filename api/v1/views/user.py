#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    users_list = []
    users = storage.all(User)
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)

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
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201
