import logging

import os
import urlparse

import wikipedia

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "GET":
        return(render_template("index.html"))
    if request.method == "POST":
        return(render_template(
                "search_results.html",
                query = request.form['idea'],
                results = wikipedia.search(request.form['idea'], results=5)
            )
        )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
