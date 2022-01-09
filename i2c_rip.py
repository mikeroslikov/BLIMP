import subprocess
import re

data=""
i=''
for i in range(0,256):
    data+=str(subprocess.check_output("i2cget -y 1 0x1e "+hex(i),stderr=subprocess.STDOUT, shell = True))
    #data.append()
print(re.findall(r"0x..", data))