import DataProcess
import Datapath
import json
import pprint
import requests
import response
import sseclient  # pip install sseclient-py
import flask
from flask import request, jsonify, Flask, render_template, Response, stream_with_context
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Raw data from the Jetson
@app.route('/raw-data')
def progress():
    def generate():
        url = 'http://192.168.50.207:8080/tracker/sse'

        stream_response = requests.get(url, stream=True)
        client = sseclient.SSEClient(stream_response)

        for event in client.events():
            # return event.data
            result = json.loads(event.data)
            yield str(result)
            # time.sleep(0.5)

    resp = Response(generate(), mimetype='text/event-stream')
    resp.headers['Connection'] = 'keep-alive'
    # resp.headers['Transfer-Encoding'] = 'chunked'
    resp.headers['Cache-Control'] = 'no-cache'
    resp.headers['X-Powered-By'] = 'Express'
    return resp


# Gives list of all objects since inception (Name and Count)- In Progress
@app.route('/ObjectCountSinceInception')
def object_count_since_inception():
    def eventStream():

        object_names_since_inception = []
        totalIds = []
        totalCount = []
        whole_object = []

        while True:
            totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
                object_names_since_inception, totalIds, totalCount)
            yield str(json.dumps(whole_object[-1]))
            # time.sleep(1.0)
    return Response(eventStream(), mimetype='text/event-stream',)


# Gives Id, NameOfObject, X, Y, Angle of the object
@app.route('/id')
def id():
    def eventStream2():

        object_names_since_inception = []
        totalIds = []
        totalCount = []
        whole_object = []

        while True:
            totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
                object_names_since_inception, totalIds, totalCount)
            # All array elements except last element
            # Use json.dumps to add double quotes to the JSON data
            yield str(json.dumps(whole_object[:-1]))
            # time.sleep(1.0)
    return Response(eventStream2(), mimetype='text/event-stream')


# Gives list of all objects in live view (Name and Count)
@app.route('/ObjectCountLiveView')
def object_count_live_view():
    def eventStream3():

        object_names_since_inception = []
        totalIds = []
        totalCount = []
        whole_object = []

        while True:
            totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
                object_names_since_inception, totalIds, totalCount)
            # Last array element
            yield str(json.dumps(whole_object[-1]['LiveTupleWithCount']))
            # time.sleep(1.0)

    return Response(eventStream3(), mimetype='text/event-stream')

# # Backup Route File to copy
# @app.route('/carlos-data-backup')
# def carlos_data_backup():
#     def eventStream():

#         object_names_since_inception = []
#         totalIds = []
#         totalCount = []
#         whole_object = []

#         while True:
#             totalCount, object_names_since_inception, totalIds, whole_object = DataProcess.DroneLiveData(
#                 object_names_since_inception, totalIds, totalCount)
#             yield str(whole_object[-1])
#             # time.sleep(0.5)
#     return Response(eventStream(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
