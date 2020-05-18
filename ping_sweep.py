#!/usr/bin/python
import os
subnet=raw_input("Type first three octets of subnet to scan (such as \"192.168.0\":")
for x in range(1,254):
  cmd="ping -c1 " + subnet + "." + str(x) + " > /dev/null"
  res=os.system(cmd)
  if res == 0:
    print subnet + "." + str(x) + " is up"
  else:
    print subnet + "." + str(x) + " is down"
