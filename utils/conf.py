# -*- coding: utf-8 -*-

import os

ADMIN_LIST = ['830831574', '691573665']

APP_NAME = u'StopSocial'
APP_DESC = u'Jogue Stop com seus amigos...RÁ!'

FACEBOOK_APP_ID = '224407034322805'
FACEBOOK_APP_SECRET = 'ad5b4d2f3f17a06a7ff1d33af109a6b7'
EXTERNAL_HREF = 'http://stop-social.appspot.com'
FACEBOOK_CANVAS_NAME = 'social-stop'

if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    FACEBOOK_APP_ID = '282067151865906'
    FACEBOOK_APP_SECRET = '152b1c05441138786234030905ce91e6'
    EXTERNAL_HREF = 'http://localhost:8089'
    FACEBOOK_CANVAS_NAME = 'social-stop-dev'

#https://graph.facebook.com/oauth/access_token?client_id=APP_ID&client_secret=APP_SECRET&grant_type=client_credentials