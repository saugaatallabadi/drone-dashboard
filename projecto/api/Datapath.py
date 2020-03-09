import json

object_names_since_inception = []
totalIds = []
totalCount = []


def SaveToFile(JsonData):

    datafile = open('dronedata.json', 'a')
    json.dump(JsonData, datafile)


def Elements_In_Data(Data):

    Elements = []
    Id = []
    horizontalAxis = []
    verticalAxis = []
    bearing = []
    whole_object = []

    for x in range(0, len(Data['trackerDataForLastFrame']['data'])):
        Elements.append(Data['trackerDataForLastFrame']['data'][x]['name'])
        Id.append(Data['trackerDataForLastFrame']['data'][x]['id'])
        horizontalAxis.append(Data['trackerDataForLastFrame']['data'][x]['x'])
        verticalAxis.append(Data['trackerDataForLastFrame']['data'][x]['y'])
        bearing.append(Data['trackerDataForLastFrame']['data'][x]['bearing'])
        whole_object.append({"ID": Data['trackerDataForLastFrame']['data'][x]['id'],
                             "name_of_object": Data['trackerDataForLastFrame']['data'][x]['name'],
                             "x": Data['trackerDataForLastFrame']['data'][x]['x'],
                             "y": Data['trackerDataForLastFrame']['data'][x]['y'],
                             "Angle": Data['trackerDataForLastFrame']['data'][x]['bearing']
                             })

    return Elements, Id, horizontalAxis, verticalAxis, bearing, whole_object


def Number_Of_Objects(Objects):

    # Counts the number of objects received
    # returns "Number" a list of integers in order with the objects detected
    # returns "CheckList" a list of string with the name of the objects detected, in
    # this list there are no repeated objects

    numberOfObjects = []
    objectType = []

    for x in range(0, len(Objects)):
        if Objects[x] not in objectType:
            numberOfObjects.append(Objects.count(Objects[x]))
            objectType.append(Objects[x])

    return numberOfObjects, objectType


def DataForDisplaying(whole_object, quantityOfObjects, objectsOnDisplay, Id, name_of_object, Objects, totalCount, object_names_since_inception, totalIds):

    differences = [item for item in Id if not item in totalIds]
    objectDiff = []
    numberDiffLocation = []
    nameOfDiff = []

    if differences:

        for x in range(0, len(differences)):
            totalIds.append(differences[x])
        # for x in range (0,len(Id)):
        #     for y in range (0,len(differences)):
        #         if Id[x]==differences[y]:
        #             objectDiff.append(x)
        for x in range(0, len(differences)):
            objectDiff.append(Id.index(differences[x]))

        nameOfDiff = [
            item for item in name_of_object if not item in object_names_since_inception]
        if nameOfDiff:
            for x in nameOfDiff:
                object_names_since_inception.append(x)
            for x in objectDiff:
                numberDiffLocation.append(
                    object_names_since_inception.index(Objects[x]))
            for x in range(0, len(nameOfDiff)):
                totalCount.append(0)
            for x in range(0, len(differences)):
                totalCount[numberDiffLocation[x]
                           ] = totalCount[numberDiffLocation[x]]+1

    return totalCount, object_names_since_inception, totalIds


def DataGathering(totalCount, object_names_since_inception, totalIds, whole_object, Data, Objects, quantityOfObjects, name_of_object):

    for x in range(0, len(Data['trackerDataForLastFrame']['data'])):

        whole_object.append({"object_names_since_inception": object_names_since_inception, "each_object_count_since_inception": totalCount, name_of_object[x]: quantityOfObjects[x],
                             "objects_names_in_current_view": Objects, "object_count_in_current_view": len(Objects), "object_names_in_current_view": name_of_object, "each_object_count_in_current_view": quantityOfObjects})

        return whole_object


#
# def main():
#
#     # callSendToAzure()
#     # initialize the SSE client
#
#     url = 'http://192.168.50.207:8080/tracker/sse'
#     stream_response = requests.get(url, stream=True)
#     client = sseclient.SSEClient(stream_response)
#
#     # this loops gets the data stream from the Jetson Nano
#
#     for event in client.events():
#         # transform data into Json Format
#         Data = json.loads(event.data)
#         Objects, Id , x ,y, bearing,whole_object = Elements_In_Data(Data)
#         quantityOfObjects, name_of_object = Number_Of_Objects(Objects)
#         DataForDisplaying(whole_object,quantityOfObjects,name_of_object,Id,name_of_object,Objects)
#         #TotalNumberOfObjects(newID,Objects,name_of_object)
#         #SendToAzure.SendEvery("HostName=WellnessHub.azure-devices.net;DeviceId=Drone;SharedAccessKey=pbWAdY2W5QW2FJcCDJckZ6HAqF/ShM7DBpPWdNzg3pA=")
#         print(name_of_object)
#
# main()
