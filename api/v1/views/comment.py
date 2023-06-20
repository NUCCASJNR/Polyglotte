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

@app_views.route("/comments/<comment_id>", methods=["GET"], strict_slashes=False)
def get_one_comment(comment_id):
    """
    Retrieves one comment using the comment id
    """
    comment = storage.get(Comment, comment_id)
    if comment:
        return jsonify(comment.to_dict())
    abort(404)


@app_views.route("/comments/<comment_id>", methods=["DELETE"], strict_slashes=False)
def delete_one_comment(comment_id):
    """
    Deletes a Comment using the comment id
    """

    comment = storage.get(Comment, comment_id)
    if comment:
        comment.delete()
        storage.save()
        return jsonify({"Status": "Comment Successfully deleted!"})
    abort(404)

@app_views.route("/posts/<post_id>/comments", methods=["POST"],
                 strict_slashes=False)
def post_comment(post_id):
    """
    Posts a New comment
    """
    comment_list = []
    post = storage.get(BlogPost, post_id)
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Not a JSON"})
    if "user_id" not in post_data:
        return jsonify({"error": "Missing user_id"})
    if "post_id" not in post_data:
        return jsonify({"error": "Missing post_id"})
    if "content" not in post_data:
        return jsonify({"error": "Missing Comment content"})
    if not post:
        abort(404)
    comment = Comment()
    for key, value in post_data.items():
        setattr(comment, key, value)
    comment.save()
    return jsonify(comment.to_dict()), 201