import socket
import sys
import time

throttle_position=1000
throttle_min =0
throttle_max = 0xffff



from tkinter import *
master = Tk()
master.geometry("500x500")
master.columnconfigure(0, weight=1)
master.rowconfigure(0, weight=1)
w1 = Scale(master, from_=throttle_min, to=throttle_max, tickinterval=10)
w1.set(throttle_min)
w1.pack(fill=BOTH)

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
            connection.sendall(w1.get().to_bytes(2, byteorder='big'))
            time.sleep(0.1)
            master.update_idletasks()
            master.update()
            
    finally:
        # Clean up the connection
        connection.close()
