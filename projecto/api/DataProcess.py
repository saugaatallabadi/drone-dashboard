import sseclient
import json
import Datapath
import requests


def DroneLiveData(object_names_since_inception, totalIds, totalCount):

    url = 'http://192.168.50.207:8080/tracker/sse'
    stream_response = requests.get(url, stream=True)
    client = sseclient.SSEClient(stream_response)

    # this loops gets the data stream from the Jetson Nano

    for event in client.events():
        # transform data into Json Format
        Data = json.loads(event.data)
        Objects, Id, x, y, bearing, whole_object = Datapath.Elements_In_Data(
            Data)
        quantityOfObjects, name_of_object = Datapath.Number_Of_Objects(Objects)
        totalCount, object_names_since_inception, totalIds = Datapath.DataForDisplaying(
            whole_object, quantityOfObjects, name_of_object, Id, name_of_object, Objects, totalCount, object_names_since_inception, totalIds)
        whole_object = Datapath.DataGathering(
            totalCount, object_names_since_inception, totalIds, whole_object, Data, Objects, quantityOfObjects, name_of_object)

        return totalCount, object_names_since_inception, totalIds, whole_object
