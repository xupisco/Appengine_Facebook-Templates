# -*- coding: utf-8 -*-
import os

ADMIN_LIST = ['1', '2']

APP_NAME = u'App Name'
APP_DESC = u'App Desc'

FACEBOOK_APP_ID = 'REAL_FB_APP_ID'
FACEBOOK_APP_SECRET = 'REAL_FB_APP_SECRET'
EXTERNAL_HREF = 'APP_URL'  # WITHOUT trailing slash
FACEBOOK_CANVAS_NAME = 'REAL_FB_CANVAS_NAME'

if os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    FACEBOOK_APP_ID = 'DEV_FB_APP_ID'
    FACEBOOK_APP_SECRET = 'DEV_FB_APP_SECRET'
    EXTERNAL_HREF = 'DEV_APP_URL'
    FACEBOOK_CANVAS_NAME = 'DEV_FB_CANVAS_NAME-stop-dev'

# How to get APP credentials
# https://graph.facebook.com/oauth/access_token?client_id=APP_ID&client_secret=APP_SECRET&grant_type=client_credentials