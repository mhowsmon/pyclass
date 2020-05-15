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
output = net_connect.send_command(command, expect_string=r'Protocol \[ip\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'Target IP address:')
print(output)
output = net_connect.send_command('8.8.8.8', expect_string=r'Repeat count \[5\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'Datagram size \[100\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'Timeout in seconds \[2\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'Extended commands \[n\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'Sweep range of sizes \[n\]:')
print(output)
output = net_connect.send_command('\n', expect_string=r'#')
print(output)
net_connect.disconnect()

''' his code, more efficient

import os
from getpass import getpass
from netmiko import ConnectHandler

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
device = {
    "device_type": "cisco_ios",
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
}
net_connect = ConnectHandler(**device)

output = net_connect.send_command(
    "ping", expect_string=r"Protocol", strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Target IP", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "8.8.8.8", expect_string=r"Repeat count", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Datagram size", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Timeout in seconds", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Extended commands", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"Sweep range of sizes", strip_prompt=False, strip_command=False
)
output += net_connect.send_command(
    "\n", expect_string=r"#", strip_prompt=False, strip_command=False
)
net_connect.disconnect()

print()
print(output)
print()

'''

