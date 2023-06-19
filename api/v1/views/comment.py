#!/usr/bin/python3

"""
HAndles All APIs for comments
"""
from models import storage
from models.comment import Comment
from models.blog_post import BlogPost
from flask import jsonify, abort, request
from api.v1.views import app_views

@app_views.route("/comments", methods=["GET"], strict_slashes=False)
def get_comments():
    """
    Get comments
    """
    comment_list = []
    comments = storage.all(Comment)
    for comment in comments.values():
        comment_list.append(comment.to_dict())
    return jsonify(comment_list)