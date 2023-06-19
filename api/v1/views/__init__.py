#!/usr/bin/python3

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.user import *
from api.v1.views.stats import *
from api.v1.views.blog_post import *
from api.v1.views.comment import *