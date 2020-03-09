import json
import pprint
import requests
import sseclient  # pip install sseclient-py
import asyncio
import random
import datetime
import websockets

dataState = []
url = 'http://192.168.50.207:8080/tracker/sse'
stream_response = requests.get(url, stream=True)

client = sseclient.SSEClient(stream_response)


def appendData():
    # Loop forever (while connection "open")
    for event in client.events():
        print('p')
        # print("got a new event from server")
        dataState.append(event.data)


async def handler(websocket, path):
    while True:
        data = [
            {
                "name": "Random Int 1",
                "number": random.randint(0, 1000)
            },
            {
                "name": "Random Int 2",
                "number": random.randint(1001, 2000)
            },
            {
                "name": "Random Int 3",
                "number": random.randint(2001, 3000)
            }
        ]
        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)

start_server = websockets.serve(handler, "127.0.0.1", 8889)
asyncio.get_event_loop().run_until_complete(start_server)

appendData()
asyncio.get_event_loop().run_forever()
