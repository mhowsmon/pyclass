#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from netmiko import ConnectHandler
from datetime import datetime
import time

device1 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_ios',
    'secret':'88newclass',
    'session_log':'my_output.txt'
}


net_connect = (ConnectHandler(**device1))
output = net_connect.find_prompt()
print(output)
output = net_connect.config_mode()
print(output)
output = net_connect.find_prompt()
print(output)
output = net_connect.exit_config_mode()
print(output)
output = net_connect.write_channel("disable\n")
print(output)
time.sleep(2)
output = net_connect.read_channel()
print(output) 
output = net_connect.enable()
print(output)
net_connect.disconnect()

''' his code
import os
import time
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**device)
print("\nCurrent Prompt: ")
print(net_connect.find_prompt())

print("\nEnter Config Mode, Current Prompt: ")
net_connect.config_mode()
print(net_connect.find_prompt())

print("\nExit Config Mode, Current Prompt: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())

print("\nExit privileged exec (disable), Current Prompt: ")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)

print("\nRe-enter enable mode, Current Prompt: ")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
print()
'''
