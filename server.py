import asyncio
import websockets

# Create handler for each connection
async def handler(websocket, path):
    client_ip, client_port = websocket.remote_address
    data = await websocket.recv()
    print(data)
    reply = f"Connection from address => {client_ip}:{client_port}"
    await websocket.send(reply)

print("Server starting...")
# Start the server
start_server = websockets.serve(handler, "0.0.0.0", 8000)
print("Server Started")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
