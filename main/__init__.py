# -*- coding: utf-8 -*-
import webapp2  # Template engine
from main import main

_DEBUG = True

app = webapp2.WSGIApplication([
        ('/', main.Main),
        ('/connect', main.Connect),
], debug=_DEBUG)
