#!/usr/bin/python3
"""
Init file
"""

from models.engine.storage import Storage
from models.base_model import Base, BaseModel
from models.user import User
from models.blog_post import BlogPost
from models.comment import Comment
from models.follower import Follower
storage = Storage()
storage.reload()
storage.all()
