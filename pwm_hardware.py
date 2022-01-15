from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.servo[0].actuation_range = 180
kit.servo[0].set_pulse_width_range(1000, 2000)

while True:
    for i in range(0,180):
	    kit.servo[0].angle = i
	    time.sleep(0.1)
    for i in range(180,0):
	    kit.servo[0].angle = i
	    time.sleep(0.1)