#!/usr/bin/env python
from pprint import pprint

device1 = {
   'host':'cisco3.lasthop.io',
   'username':'someuser',
   'password':'somepass',
   'device_type':'cisco_xe',
   'secret':'somepass'
}
device2 = {
   'host':'cisco4.lasthop.io',
   'username':'someuser',
   'password':'somepass',
   'device_type':'cisco_xe',
   'secret':'somepass'
}
device3 = {
   'host':'nxos1.lasthop.io',
   'username':'someuser',
   'password':'somepass',
   'device_type':'cisco_nxos',
   'secret':'somepass'
}
device4 = {
   'host':'nxos2.lasthop.io',
   'username':'someuser',
   'password':'somepass',
   'device_type':'cisco_nxos',
   'secret':'somepass'
}

devicelist = []
devicelist.append(device1)
devicelist.append(device2)
devicelist.append(device3)
devicelist.append(device4)

print(type(devicelist))
print(len(devicelist))
