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

net_connect = (ConnectHandler(**device1))
print(net_connect.find_prompt())

''' His example

import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
net_connect = ConnectHandler(
    host="cisco3.lasthop.io",
    username="pyclass",
    password=password,
    device_type="cisco_ios",
    session_log="my_session.txt",
)

print(net_connect.find_prompt())
net_connect.disconnect()


'''

