import logging
import os
import urlparse

import wikipedia
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = False


@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "GET":
        return(render_template("index.html"))
    if request.method == "POST":
        return(render_template("map_view.html",
                               query=request.form['idea'],
                               results=wikipedia.search(request.form['idea'],
                                                        results=5)
                               )
               )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
