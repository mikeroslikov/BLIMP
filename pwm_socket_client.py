import socket
import sys

import time


import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 50
led_channel = hat.channels[0]
#led_channel.duty_cycle = 0xffff
#led_channel.duty_cycle = 0


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("192.168.0.94",10000)
print("connecting to" + str(server_address))
sock.connect(server_address)

while True:
    while True:
        data = int.from_bytes(sock.recv(16), byteorder='big')
        print("received "+ str(data))
        led_channel.duty_cycle = data
			
finally:
print("closing socket")
sock.close()