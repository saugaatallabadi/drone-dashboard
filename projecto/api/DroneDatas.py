import DataProcess
import pprint

totalOfObjects = []
totalIds = []
totalCount = []
wholeData = []

while True:
    # pprint.pprint(DataProcess.DroneLiveData(
    #     totalOfObjects, totalIds, totalCount))
    # totaDataProcess.DroneLiveData(
    #     totalOfObjects, totalIds, totalCount))

    totalCount, totalOfObjects, totalIds, wholeData = DataProcess.DroneLiveData(
        totalOfObjects, totalIds, totalCount)

    pprint.pprint(wholeData)
