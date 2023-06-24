#!/usr/bin/python3

"""
Defines the database Storage class
"""

from models import storage
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy

from models.user import User
from models.comment import Comment
from models.follower import Follower
from models.blog_post import BlogPost
from models.base_model import BaseModel, Base

classes = {
    "user": User,
    "comment": Comment,
    "blog_post": BlogPost,
    "follower": Follower
}


class Storage:
    """
    The Database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Init method
        """
        # Get enviroment variables
        # BLOG_MYSQL_USER = getenv("BLOG_MYSQL_USER")
        # BLOG_MYSQL_PWD = getenv("BLOG_MYSQL_PWD")
        # BLOG_MYSQL_HOST = getenv("BLOG_MYSQL_HOST")
        # BLOG_MYSQL_DB = getenv("BLOG_MYSQL_DB")
        # BLOG_ENV = getenv("BLOG_ENV")

        # Create SQLAlchemy engine instance
        # self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
        #                               format(BLOG_MYSQL_USER,
        #                                      BLOG_MYSQL_PWD,
        #                                      BLOG_MYSQL_HOST,
        #                                      BLOG_MYSQL_DB))
        # # Drop all tables in the database if in test enviroment
        # if getenv('BLOG_ENV') == 'test':
        #     Base.metadata.drop_all(bind=self.__engine)

        self.__engine = create_engine('mysql+mysqldb://blog_dev:blog_dev_pwd@localhost:3306/blog_dev_db')

        # Drop all tables in the database if in test enviroment
        if getenv('BLOG_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query the current database session
        """
        query_dict = {}

        if cls:
            objs = self.__session.query(cls)
            for obj in objs:
                query_dict[obj.__class__.__name__ + '.' + obj.id] = obj

        else:
            for key, value in classes.items():
                objs = self.__session.query(value)
                for obj in objs:
                    query_dict[obj.__class__.__name__ + '.' + obj.id] = obj

        return query_dict

    def new(self, obj):
        """
        Adds the new obj to database
        """
        self.__session.add(obj)

    def save(self):
        """
        Saves the present connection to database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes the current object
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads the current database connection
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
        closes the current session
        """

        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieves one object
        """
        if cls not in classes.values():
            return None
        objects = storage.all(cls)
        for val in objects.values():
            if val.id == id:
                return val
        return None

    def count(self, cls=None):
        """
        count the number of objects in storage:
        """
        count = self.all(cls)
        if cls in classes.values():
            count = self.all(cls)
        return len(count)
