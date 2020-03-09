import DataProcess
import Datapath
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


@app.route('/raw-data')
def progress():
    def generate():
        url = 'http://192.168.50.207:8080/tracker/sse'
        stream_response = requests.get(url, stream=True)
        client = sseclient.SSEClient(stream_response)

        for event in client.events():
            # return event.data
            result = json.loads(event.data)
            yield str(result['trackerDataForLastFrame']['data'][0]['bearing'])
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')


@app.route('/carlos-data')
def carlos_data():
    def eventStream():

        object_names_since_inception = []
        totalIds = []
        totalCount = []
        whole_object = []

        while True:
            totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
                object_names_since_inception, totalIds, totalCount)
            # pprint.pprint(whole_object)
            yield str(whole_object)
            time.sleep(0.5)
    return Response(eventStream(), mimetype='text/event-stream')


@app.route('/saugaat-data')
def saugaat_data():
    def eventStream2():

        object_names_since_inception = []
        totalIds = []
        totalCount = []
        whole_object = []

        while True:
            totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
                object_names_since_inception, totalIds, totalCount)
            # pprint.pprint(whole_object)
            yield str(whole_object)
            time.sleep(0.5)
    return Response(eventStream2(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(debug=True)
