import asyncio
import websockets
async def test():
    try:
        async   with websockets.connect('ws://116.203.199.46:8000') as websocket:
            try:
                await websocket.send("Guy")
                response = await websocket.recv()
                print(response)
            except websockets.exceptions.WebSocketException as e:
                print("Connection backup closed-WebSocketException->", e)
    except BaseException as ex:
        print("Connection closed-BaseException->", ex)
asyncio.get_event_loop().run_until_complete(test())
