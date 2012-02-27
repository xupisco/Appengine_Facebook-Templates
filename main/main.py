# -*- coding: utf-8 -*-
_DEBUG = True

import webapp2 # Template engine
from functools import wraps

from utils.base import CoreHandler
from utils import conf

def user_required(fn):
    """Decorator to ensure a user is present"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        handler = args[0]
        if handler.user:
            return fn(*args, **kwargs)

        handler.redirect(u'/connect')
    return wrapper


class Connect(CoreHandler):
    def get(self):
        if not self.user:
            if 'dev' in conf.FACEBOOK_CANVAS_NAME:
                auth_url = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://localhost:8089/&scope=email,publish_stream' % conf.FACEBOOK_APP_ID
            else:
                auth_url = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://apps.facebook.com/%s/&scope=email,publish_stream' % (conf.FACEBOOK_APP_ID, conf.FACEBOOK_CANVAS_NAME)
            self.generate('connect.html', { 'auth_url': auth_url })
        else:
            self.redirect('/')


class Main(CoreHandler):
    @user_required
    def get(self):
        self.generate('index.html')


app = webapp2.WSGIApplication([('/', Main),
                               ('/connect', Connect),
                              ],
                               debug=_DEBUG);