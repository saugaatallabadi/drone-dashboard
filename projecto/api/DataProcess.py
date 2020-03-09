import sseclient
import json
import Datapath
import requests

totalOfObjects = []
totalIds = []
totalCount = []
wholeData = []


def DroneLiveData(totalOfObjects, totalIds, totalCount):

    url = 'http://192.168.50.207:8080/tracker/sse'
    stream_response = requests.get(url, stream=True)
    client = sseclient.SSEClient(stream_response)

    # this loops gets the data stream from the Jetson Nano

    for event in client.events():
        # transform data into Json Format
        Data = json.loads(event.data)
        Objects, Id, x, y, bearing, wholeObject = Datapath.Elements_In_Data(
            Data)
        quantityOfObjects, nameOfObject = Datapath.Number_Of_Objects(Objects)
        totalCount, totalOfObjects, totalIds = Datapath.DataForDisplaying(
            wholeObject, quantityOfObjects, nameOfObject, Id, nameOfObject, Objects, totalCount, totalOfObjects, totalIds)
        wholeObject = Datapath.DataGathering(
            totalCount, totalOfObjects, totalIds, wholeObject, Data, Objects, quantityOfObjects, nameOfObject)

        return totalCount, totalOfObjects, totalIds, wholeObject
