# -*- coding: utf-8 -*-

from app import app
from flask import Flask, request, jsonify
import base64, hmac, hashlib
import ssl
import urllib


@app.route('/healthcheck')
def healthcheck():
    return "okey"
