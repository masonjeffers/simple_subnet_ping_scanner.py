#!/usr/bin/python
import os
ping = "ping -c1 10.11.1."
devnull = " > /dev/null"
for x in range(1,5):
    x=str(x)
    cmd=ping+x+devnull
    res=os.system(cmd)
    if res == 0:
      print '192.168.0.'+str(x), "is up"
    else:
        print '192.168.0.'+str(x), "is down"

