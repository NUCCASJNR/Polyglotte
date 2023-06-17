#!/usr/bin/python3

from flask import BluePrint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.user import *
