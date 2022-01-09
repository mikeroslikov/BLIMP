#!/usr/bin/python
"""\
Simple g-code streaming script
"""

import serial
import time
import argparse

parser = argparse.ArgumentParser(description='This is a basic gcode sender.')
parser.add_argument('-p','--port',help='Input USB port',required=True)
args = parser.parse_args()
 
## show values ##
print ("USB Port: %s" % args.port )


# Open serial port
s = serial.Serial(args.port,9800)
print ('Opening Serial Port')

# Wake up
print ('Good Morning CNC!')
s.write("\r\n\r\n") # Hit enter a few times to wake the machine
time.sleep(2)   # Wait for machine to initialize
s.flushInput()  # Flush startup text in serial input
print ('You now have control. Ctrl+C to exit.')

while True:
    #l = raw_input("Enter gcode:")
    #l = l.strip() # Strip all EOL characters for streaming
    #if  (l.isspace()==False and len(l)>0) :
    #    s.write(l + '\n') # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    print ('' + grbl_out.strip() + '\n')


 
# Close file and serial port
f.close()
s.close()