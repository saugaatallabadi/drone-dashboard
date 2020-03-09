# WORKS!!!

import json
import pprint
import requests
import sseclient  # pip install sseclient-py
import flask
from flask import request, jsonify, Flask, render_template, Response, stream_with_context
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/progress')
def progress():
    def generate():
        # x = 0

        # while x <= 100:
        #     yield "data:" + str(x) + "\n\n"
        #     x = x + 10
        #     time.sleep(0.5)

        url = 'http://192.168.50.207:8080/tracker/sse'
        stream_response = requests.get(url, stream=True)
        client = sseclient.SSEClient(stream_response)

        for event in client.events():
            # return event.data
            result = json.loads(event.data)
            yield str(result['trackerDataForLastFrame']['data'][0]['bearing'])
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


@app.route('/progress2')
def progress2():
    def generate():
        # x = 0

        # while x <= 100:
        #     yield "data:" + str(x) + "\n\n"
        #     x = x + 10
        #     time.sleep(0.5)

        url = 'http://192.168.50.207:8080/tracker/sse'
        stream_response = requests.get(url, stream=True)
        client = sseclient.SSEClient(stream_response)

        for event in client.events():
            # return event.data
            result = json.loads(event.data)
            yield result['trackerDataForLastFrame']['data'][3]['name']
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run()
