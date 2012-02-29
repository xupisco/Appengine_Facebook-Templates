# -*- coding: utf-8 -*-
from utils import conf
from utils.base import CoreHandler
from utils.decorators import user_required


class Connect(CoreHandler):
    def get(self):
        if not self.user:
            if 'dev' in conf.FACEBOOK_CANVAS_NAME:
                import os
                host = os.environ.get('SERVER_NAME')
                port = os.environ.get('SERVER_PORT')
                auth_url = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://%s:%s/&scope=email,publish_stream' % (conf.FACEBOOK_APP_ID, host, port)
                print auth_url
            else:
                auth_url = 'https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=http://apps.facebook.com/%s/&scope=email,publish_stream' % (conf.FACEBOOK_APP_ID, conf.FACEBOOK_CANVAS_NAME)
            self.generate('connect.html', {'auth_url': auth_url})
        else:
            self.redirect('/')


class Main(CoreHandler):
    @user_required
    def get(self):
        self.generate('index.html')
