# -*- coding: utf-8 -*-
import webapp2  # Template engine
from main import view

_DEBUG = True

app = webapp2.WSGIApplication([
        ('/', view.Main),
        ('/connect', view.Connect),
], debug=_DEBUG)
