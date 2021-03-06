import socket
import sys
import time

#5%-10% duty cycle at 50Hz is the range of the ESC
max = (0xffff)*0.1
min = (0xffff)*0.05

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
            th = float(input("Throttle (%)"))
            th = ((th/100)*(max-min))+min
            th = int(th)
            connection.sendall(th.to_bytes(2, byteorder='big'))
            time.sleep(0.1)
            
    finally:
        # Clean up the connection
        connection.close()
