#!/usr/bin/python3

from flask import abort, jsonify, make_response, request

from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route("/users", methods=["GET"], strict_slashes=False)
def get_users():
    """
    Docs soon 
    """

    users_list = []
    users = storage.all(User)
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)

@app_views.route("/users/<user_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_user_using_userid(user_id):
    """
    Deletes user using the user_id
    """
    user = storage.get(User, user_id)
    if user:
        user.delete()
        storage.save()
        return jsonify({"Status": "Deleted"})
    abort(404)

@app_views.route("/users/<user_id>", methods=["GET"],
                 strict_slashes=False)
def get_user_using_userid(user_id):
    """
    Gets user using the user_id
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
    if not user_data:
        return jsonify({"Error": "Not a json"}) 
    if 'username' not in user_data:
        return jsonify({"Error": "Missing username"})
    if 'first_name' not in user_data:
        return jsonify({"Error": "Mising first name"})
    if 'last_name' not in user_data:
        return jsonify({"Error": "Missing lastname"})
    if 'password' not in user_data:
        return jsonify({"Error": "Missing password"})
    if "email" not in user_data:
        return jsonify({"Error": "Missing email"})
    user = User()
    for key, value in user_data.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """
    Updates a user using the provided user_id
    """
    user = storage.get(User, user_id)
    user_data = request.get_json()
    if not user_data:
        return jsonify({"Error": "Not a json"})
    ignore = ["id", "created_at", "updated_at"]
    if user:
        for key, value in user_data.items():
            if key not in ignore:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict()), 200
    abort(404)
