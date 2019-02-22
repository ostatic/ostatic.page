# -*- coding: utf-8 -*-

from app import app
from flask import Flask, request, jsonify
from flask import render_template
import base64, hmac, hashlib
import ssl
import urllib

@app.route('/')
def index():
    return render_template('core.html')



@app.route('/healthcheck')
def healthcheck():
    return "okey"
