import subprocess
import re
import time

data1=""
data2=""

for i in range(0,256):
    data1+=str(subprocess.check_output("i2cget -y 1 0x1e "+hex(i)+" w",stderr=subprocess.STDOUT, shell = True))
time.sleep(1)
for i in range(0,256):
    data2+=str(subprocess.check_output("i2cget -y 1 0x1e "+hex(i)+" w",stderr=subprocess.STDOUT, shell = True))
time.sleep(1)
a1=re.findall(r"0x....", data1)
a2=re.findall(r"0x....", data2)

for j in range(0,len(a1)):
    if a1[j] != a2[j]:
	    print(str(j))