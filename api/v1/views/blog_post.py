#!/usr/bin/python3
"""
API routes for blog posts
"""
from models import storage
from models.user import User
from models.blog_post import BlogPost
from flask import jsonify, abort, make_response, request
from api.v1.views import app_views

@app_views.route("/posts", methods=["GET"], strict_slashes=False)
def get_blogposts():
    """
    Gets All posts
    """
    posts_list = []
    posts = storage.all(BlogPost)
    for post in posts.values():
        posts_list.append(post.to_dict())
    return jsonify(posts_list)

@app_views.route("/posts", methods=["POST"], strict_slashes=False)
def post_blogpost():
    """
    Posts a new blog
    """
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Not a JSON"})
    post = BlogPost()
    for key, value in post_data.items():
        setattr(post, key, value)
    post.save()
    return jsonify(post.to_dict()), 201