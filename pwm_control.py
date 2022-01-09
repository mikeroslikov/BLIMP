#!/usr/bin/env python

# esc_start.py
# 2015-04-14
# Public Domain
#
# Sends the servo pulses needed to initialise some ESCs
#
# Requires the pigpio daemon to be running
#
# sudo pigpiod

import time

import pigpio

SERVO = 23
max_throttle = 2000
min_throttle = 700
pi = pigpio.pi() # Connect to local Pi.

pi.set_servo_pulsewidth(SERVO, 0) # Minimum throttle.

time.sleep(1)

for i in range(0,max_throttle):
    pi.set_servo_pulsewidth(SERVO, i)
print("max")
time.sleep(0.5)

for i in range(max_throttle,min_throttle):
    pi.set_servo_pulsewidth(SERVO, i)

print("min")
time.sleep(0.5)

for i in range(min_throttle,1100):
    pi.set_servo_pulsewidth(SERVO, i)

print("mid")
time.sleep(2)

pi.stop() # Disconnect from local Raspberry Pi.

