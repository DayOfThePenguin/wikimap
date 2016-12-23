import logging

import os
import urlparse
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "GET":
        return(render_template("index.html"))
    if request.method == "POST":
        return("<p>Hello, you requested this page with the HTTP POST method.</p>" +
        "<p>You indicated you are interested in learning about: %s</p>" %
        request.form["idea"])
