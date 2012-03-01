# -*- coding: utf-8 -*-
import os
import settings
from core.handler import CoreHandler
from utils.decorators import user_required

BASE_URL = 'http://www.facebook.com/dialog/oauth?{qs}'
BASE_QS = 'client_id={client_id}&redirect_uri={url}{perms}'


class Connect(CoreHandler):
    def get(self):
        auth_conf = {
            'perms': '&scope=email,publish_stream',
            'client_id': settings.FACEBOOK_APP_ID
        }
        if not self.user:
            if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
                host = os.environ.get('SERVER_NAME')
                port = os.environ.get('SERVER_PORT')
                auth_conf.update({
                    'url': 'http://{host}:{port}/'.format(host=host, port=port)
                })
            else:
                auth_conf.update({
                    'url': 'http://apps.facebook.com/{app}/'.format(
                        app=settings.FACEBOOK_CANVAS_NAME
                    )
                })

            auth_url = BASE_URL.format(qs=BASE_QS.format(**auth_conf))
            print auth_url
            self.generate('connect.html', {'auth_url': auth_url})
        else:
            self.redirect('/')


class Main(CoreHandler):
    @user_required
    def get(self):
        self.generate('index.html')
