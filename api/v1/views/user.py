#!/usr/bin/python3

from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response


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
