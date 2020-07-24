"""A Flash app for local testing"""

from flask import Flask, request

import main

app = Flask(__name__)

@app.route("/")
def hello():
    return main.hello(request)

@app.route("/ds")
def ds_list():
    return main.list(request)