import socket
import sys

import time

import pigpio

SERVO = 23
pi = pigpio.pi() # Connect to local Pi.

pi.set_mode(SERVO, pigpio.OUTPUT)

pi.set_PWM_frequency(SERVO,500)

pi.set_servo_pulsewidth(SERVO, 0)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.0.94",10000)
print("connecting to" + str(server_address))
sock.connect(server_address)

try:
    
    while True:
        data = int.from_bytes(sock.recv(32), byteorder='big')
        #print("received "+ str(data))
		pi.set_servo_pulsewidth(SERVO, data)

finally:
    print("closing socket")
    sock.close()
	pi.stop()