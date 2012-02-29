# -*- coding: utf-8 -*-
from functools import wraps


def user_required(fn):
    """Decorator to ensure a user is present"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        handler = args[0]
        if handler.user:
            return fn(*args, **kwargs)

        handler.redirect(u'/connect')
    return wrapper
