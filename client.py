import asyncio
import websockets
import os
import socket

# Function to initiate WebSocket connection
async def connect_to_websocket(uri, local_ip=None):
    try:
        # Create a new socket to bind to the local IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((local_ip, 0))  # Bind to the given local IP
        sock.listen(1)
        print(f"Bound to {local_ip}")

        # Pass the socket to the WebSocket client
        async with websockets.connect(uri, local_addr=(local_ip, 0)) as websocket:
            await websocket.send(f"Hello from {local_ip}")
            response = await websocket.recv()
            print(f"Response from server: {response}")
    except Exception as e:
        print(f"Connection from {local_ip} failed: {e}")
    finally:
        sock.close()

# Function to remove floating IP from the interface
def remove_floating_ip(floating_ip, interface):
    os.system(f"sudo ip addr del {floating_ip}/32 dev {interface}")
    print(f"Floating IP {floating_ip} removed from {interface}")

# Function to add floating IP back to the interface
def add_floating_ip(floating_ip, interface):
    os.system(f"sudo ip addr add {floating_ip}/32 dev {interface}")
    print(f"Floating IP {floating_ip} added to {interface}")

# Main function to make two WebSocket connections
async def main():
    ws_url = "ws://159.69.222.91:8000"  # WebSocket server URL
    real_ip = '116.203.199.46'
    floating_ip = '116.203.11.168'
    interface = 'eth0'  # Adjust to your network interface name

    # Step 1: Remove floating IP to use the real IP for the first request
    remove_floating_ip(floating_ip, interface)
    print(f"Connecting from real IP: {real_ip}")
    await connect_to_websocket(ws_url, real_ip)

    # Pause for a moment between connections
    await asyncio.sleep(2)

    # Step 2: Add floating IP to use it for the second request
    add_floating_ip(floating_ip, interface)
    print(f"Connecting from floating IP: {floating_ip}")
    await connect_to_websocket(ws_url, floating_ip)

# Run the main function
asyncio.run(main())
