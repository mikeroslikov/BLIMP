from picamera import PiCamera
from time import sleep
import os
import datetime

DATE = datetime.datetime.today().strftime("%d-%B-%Y_%H:%M")
DIRECTORY = '/home/pi/REC/'

os.system("mkdir "+DIRECTORY)
i=1
while i<13:
	os.system("libcamera-vid -t 3000 -o "+DIRECTORY+DATE+".h264")
	i+=1