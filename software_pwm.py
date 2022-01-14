import RPi.GPIO as GPIO
import time

servoPIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
	for i in range(0,100)
		p.ChangeDutyCycle(i/10)
		time.sleep(0.1)
	for i in range(100,0)
		p.ChangeDutyCycle(i/10)
		time.sleep(0.1)
    
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()