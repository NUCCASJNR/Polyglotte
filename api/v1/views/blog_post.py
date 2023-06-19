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

@app_views.route("/posts/<post_id>", methods=["GET"], strict_slashes=False)
def get_blogpost_using_postid(post_id):
    """
    Retrieves a post using the post id
    """
    posts = storage.get(BlogPost, post_id)
    if posts:
        return jsonify(posts.to_dict())
    abort(404)

@app_views.route("/posts/<user_id>/posts", methods=["GET"], strict_slashes=False)
def get_all_posts_of_user(user_id):
    # k = 'User.{}'.format(user_id)
    # posts =[]
    # if k not in storage.all(User):
    #     abort(404)
    # for value in storage.all(BlogPost).values():
    #     if value.to_dict()['user_id'] == user_id:
    #         posts.append(value.to_dict())
    # return jsonify(posts)
    post_list = []
    user = storage.get(User, user_id)
    if user:
        for post in storage.all(BlogPost).values():
            if post.user_id == user_id:
                post_list.append(post.to_dict())
        return jsonify(post_list), 200
    abort(404)
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