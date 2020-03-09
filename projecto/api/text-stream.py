import json
import pprint
import requests
import sseclient  # pip install sseclient-py
import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    url = 'http://192.168.50.207:8080/tracker/sse'
    stream_response = requests.get(url, stream=True)
    client = sseclient.SSEClient(stream_response)

    for event in client.events():
        # return event.data
        result = event.data
        # return jsonify(result)

    return result

    # return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/hello', methods=['GET'])
def hello():
    # url = 'http://192.168.50.207:8080/tracker/sse'
    x = requests.get('https://w3schools.com')
    return(str(x.status_code))


app.run()
