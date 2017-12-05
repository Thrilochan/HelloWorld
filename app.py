#!/usr/bin/env python
from __future__ import print_function


import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

#flask app should define in globla layout
app = Flask(__name__)
