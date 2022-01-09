import socket
import sys
import time

throttle_position=1000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("192.168.0.94",10000)
print ( "starting up "+ str(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print ("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print("connection from"+ str(client_address))

        # Receive the data in small chunks and retransmit it
        while True:
            connection.sendall(throttle_position)
            time.sleep(0.1)
            
    finally:
        # Clean up the connection
        connection.close()
