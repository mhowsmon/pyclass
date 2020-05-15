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

''' His example

import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device1 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios_telnet",
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())
net_connect.disconnect()

'''

