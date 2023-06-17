#!/usr/bin/python3
"""
Init file
"""

from models.engine.storage import Storage
storage = Storage()
storage.reload()
storage.all()
