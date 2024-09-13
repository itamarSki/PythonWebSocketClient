import asyncio
import websockets
# create handler for each connection
async def handler(websocket, path):
    data = await websocket.recv()
    print(data)
    reply = f"Data Backup recieved as:  {data}!"
    await websocket.send(reply)

print("server starting...")
start_server = websockets.serve(handler, "0.0.0.0", 8000)
print("Server Started")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
