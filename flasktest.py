#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "This is a test to see if we are able to see the website protype"

app.run(host="0.0.0.0", port=80)

