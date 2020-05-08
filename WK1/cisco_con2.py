#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
    'session_log':'my_session.txt'
}

device2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
    'session_log':'my_session.txt'
}

devicelist = []
devicelist.append(device1)
devicelist.append(device2)
for device in devicelist:
    net_connect = (ConnectHandler(**device))
    print(net_connect.find_prompt())
