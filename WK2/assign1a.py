#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_xe',
    #'session_log':'my_session.txt'
}

net_connect = (ConnectHandler(**device1))
command = "ping"
print(command)
output = net_connect.send_command_timing(command)
print(output)
output = net_connect.send_command_timing('\r')
print(output)
output = net_connect.send_command_timing('8.8.8.8\r')
print(output)
output = net_connect.send_command_timing('\r')
print(output)
output = net_connect.send_command_timing('\r')
print(output)
output = net_connect.send_command_timing('\r')
print(output)
output = net_connect.send_command_timing('\r')
print(output)
output = net_connect.send_command_timing('\r')
print(output)
net_connect.disconnect()
