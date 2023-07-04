#!/usr/bin/python3

"""
HAndles All APIs for comments
"""
from flask import abort, jsonify, request

from Clean_Blog import app_views
from models import storage
from models.blog_post import BlogPost
from models.comment import Comment
from models.user import User


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


@app_views.route("/posts/<post_id>/comments", methods=["GET"],
                  strict_slashes=False)
def get_all_comments_of_a_post(post_id):
    """
    Gets all the comments made on a post
    """
    comments_list = []
    post = storage.get(BlogPost, post_id)
    if post:
        for comment in storage.all(Comment).values():
            if comment.post_id == post_id:
                comments_list.append(comment.to_dict())
        return jsonify(comments_list)
    abort(404)
    

@app_views.route("/posts/<user_id>/<post_id>/comments", methods=["GET"],
                  strict_slashes=False)
def get_comments_of_user_on_a_post(user_id, post_id):
    """
    Gets all the comments made on a post by a user
    """
    comments_list = []
    user = storage.get(User, user_id)
    post = storage.get(BlogPost, post_id)
    if user and post:
        for comment in storage.all(Comment).values():
            if comment.user_id == user_id and comment.post_id == post_id:
                comments_list.append(comment.to_dict())
        return jsonify(comments_list)
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


@app_views.route("/comments/<comment_id>", methods=["PUT"],
                 strict_slashes=False)
def update_comments(comment_id):
    """
    Edit comments on a post
    """
    comment = storage.get(Comment, comment_id)
    comment_data = request.get_json()
    if not comment_data:
        return jsonify({"error": "Not a JSON"})
    ignore = ["id", "created_at", "updated_at"]
    if comment:
        for key, value in comment_data.items():
            if key not in ignore:
                setattr(comment, key, value)
        comment.save()
        return jsonify(comment.to_dict()), 200
    abort(404)   