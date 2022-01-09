from picamera import PiCamera
from time import sleep
import pathlib
from time import sleep
import datetime

DATE = datetime.datetime.today().strftime("%d-%B-%Y_%H:%M")
DIRECTORY = '/home/pi/REC/' + DATE
pathlib.Path(DIRECTORY).mkdir(parents=True, exist_ok=True) 
camera = PiCamera()

camera.start_recording(DIRECTORY + '/TIMG_{0:05d}.h264'.format(i))
sleep(5)
camera.stop_recording()
