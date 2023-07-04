# !/usr/bin/python3
"""
API routes for blog posts
"""
from flask import abort, jsonify, request

from Clean_Blog import app_views
from models import storage
from models.blog_post import BlogPost
from models.user import User


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


@app_views.route("/posts/<post_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_post_using_postid(post_id):
    """
    Deletes a post using post_id
    """
    post = storage.get(BlogPost, post_id)
    if post:
        post.delete()
        storage.save()
        return jsonify({"status": "Post deleted"})
    abort(404)


@app_views.route("/posts/<user_id>/posts", methods=["GET"], strict_slashes=False)
def get_all_posts_of_user(user_id):
    post_list = []
    user = storage.get(User, user_id)
    if user:
        for post in storage.all(BlogPost).values():
            if post.user_id == user_id:
                post_list.append(post.to_dict())
        return jsonify(post_list), 200
    abort(404)


@app_views.route("/posts/<user_id>/posts", methods=["DELETE"],
                 strict_slashes=False)
def delete_all_posts_of_a_user(user_id):
    user = storage.get(User, user_id)
    post_list = []
    if user:
        for post in storage.all(BlogPost).values():
            if post.user_id == user_id:
                user.delete()
                storage.save()
        return jsonify({"status": "Post deleted"})
    abort(404)


@app_views.route("/posts", methods=["POST"], strict_slashes=False)
def post_blogpost():
    """
    Posts a new blog
    """
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Not a JSON"})
    if 'user_id' not in post_data:
        return jsonify({"error": "Missing user_id"})
    if 'content' not in post_data:
        return jsonify({"error": "Missing Blog Post content"})
    if 'title' not in post_data:
        return jsonify({"error": "Missing Blog Post title"})
    if 'category' not in post_data:
        return jsonify({"error": "Missing Blog Category"})
    post = BlogPost()
    for key, value in post_data.items():
        setattr(post, key, value)
    post.save()
    return jsonify(post.to_dict()), 201


@app_views.route("/posts/<post_id>", methods=["PUT"],
                 strict_slashes=False)
def update_posts(post_id):
    """
    Updates a Blog Post
    """
    post = storage.get(BlogPost, post_id)
    post_data = request.get_json()
    if not post_data:
        return jsonify({"error": "Not a JSON"})
    ignore = ["id", "created_at", "updated_at"]
    if post:
        for key, value in post_data.items():
            if key not in ignore:
                setattr(post, key, value)
        post.save()
        return jsonify(post.to_dict()), 200
    abort(404)
