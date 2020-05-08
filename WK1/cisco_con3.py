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
getcmd = net_connect.send_command('show version')

f = open("showver.txt", mode="w")
f.write(getcmd)
f.close
