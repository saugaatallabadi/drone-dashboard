import DataProcess
import pprint

totalOfObjects = []
totalIds = []
totalCount = []
wholeData = []

totalCount, totalOfObjects, totalIds, wholeData = DataProcess.DroneLiveData(
    totalOfObjects, totalIds, totalCount)

while True:
    print(DataProcess.DroneLiveData(totalOfObjects, totalIds, totalCount))

    # pprint.pprint(DataProcess.DroneLiveData(
    #     totalOfObjects, totalIds, totalCount))
    # totaDataProcess.DroneLiveData(
    #     totalOfObjects, totalIds, totalCount))
