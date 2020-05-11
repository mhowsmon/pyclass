#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
    #'session_log':'my_session.txt'
}

net_connect = (ConnectHandler(**device1))
command = "show ip interface brief"

output = net_connect.send_command(command, use_textfsm=True)
print(output)
