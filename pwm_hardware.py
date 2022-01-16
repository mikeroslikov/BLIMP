import time

import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)
hat.frequency = 50
led_channel = hat.channels[0]
led_channel.duty_cycle = 0xffff
led_channel.duty_cycle = 0

while True:
    # Increase brightness:
    for i in range(0,0xffff,10):
        led_channel.duty_cycle = i

    # Decrease brightness:
    for i in range(0xffff, 0, -10):
        led_channel.duty_cycle = i