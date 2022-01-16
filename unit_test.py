import socket
import sys
import time

#5%-10% duty cycle at 50Hz is the range of the ESC
max = (0xffff)*0.1
min = (0xffff)*0.05
        
while True:
    th = float(input("Throttle (%)"))
    th = ((th/100)*(max-min))+min
    th = int(th)
    print(str(th))
    time.sleep(0.1)
