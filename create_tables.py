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
all_objects = storage.all()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import Base

# Create the engine
engine = create_engine('mysql+mysqldb://root:Alareef123@@localhost/blog_dev_db')

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

# Create the tables
Base.metadata.create_all(bind=engine)

# Commit the changes to the database
session.commit()
