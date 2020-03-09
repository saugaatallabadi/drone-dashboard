import json

totalOfObjects = []
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
    wholeObject = []

    for x in range(0, len(Data['trackerDataForLastFrame']['data'])):
        Elements.append(Data['trackerDataForLastFrame']['data'][x]['name'])
        Id.append(Data['trackerDataForLastFrame']['data'][x]['id'])
        horizontalAxis.append(Data['trackerDataForLastFrame']['data'][x]['x'])
        verticalAxis.append(Data['trackerDataForLastFrame']['data'][x]['y'])
        bearing.append(Data['trackerDataForLastFrame']['data'][x]['bearing'])
        wholeObject.append({"ID": Data['trackerDataForLastFrame']['data'][x]['id'],
                            "NameOfObject": Data['trackerDataForLastFrame']['data'][x]['name'],
                            "x": Data['trackerDataForLastFrame']['data'][x]['x'],
                            "y": Data['trackerDataForLastFrame']['data'][x]['y'],
                            "Angle": Data['trackerDataForLastFrame']['data'][x]['bearing']
                            })

    return Elements, Id, horizontalAxis, verticalAxis, bearing, wholeObject


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


def DataForDisplaying(wholeObject, quantityOfObjects, objectsOnDisplay, Id, nameOfObject, Objects, totalCount, totalOfObjects, totalIds):

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
            item for item in nameOfObject if not item in totalOfObjects]
        if nameOfDiff:
            for x in nameOfDiff:
                totalOfObjects.append(x)
            for x in objectDiff:
                numberDiffLocation.append(totalOfObjects.index(Objects[x]))
            for x in range(0, len(nameOfDiff)):
                totalCount.append(0)
            for x in range(0, len(differences)):
                totalCount[numberDiffLocation[x]
                           ] = totalCount[numberDiffLocation[x]]+1

    return totalCount, totalOfObjects, totalIds


def DataGathering(totalCount, totalOfObjects, totalIds, wholeObject, Data, Objects, quantityOfObjects, nameOfObject):

    for x in range(0, len(Data['trackerDataForLastFrame']['data'])):

        wholeObject.append({"TotalOfObjects": totalOfObjects, "totalCountOfObjects": totalCount,
                            "AllObjectsInView": Objects, "TotalOfObjectsInView": len(Objects), "ObjectsInView": nameOfObject, "CountPerObjectInView": quantityOfObjects})

        return wholeObject


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
#         Objects, Id , x ,y, bearing,wholeObject = Elements_In_Data(Data)
#         quantityOfObjects, nameOfObject = Number_Of_Objects(Objects)
#         DataForDisplaying(wholeObject,quantityOfObjects,nameOfObject,Id,nameOfObject,Objects)
#         #TotalNumberOfObjects(newID,Objects,nameOfObject)
#         #SendToAzure.SendEvery("HostName=WellnessHub.azure-devices.net;DeviceId=Drone;SharedAccessKey=pbWAdY2W5QW2FJcCDJckZ6HAqF/ShM7DBpPWdNzg3pA=")
#         print(nameOfObject)
#
# main()
