#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from netmiko import ConnectHandler
from datetime import datetime

device1 = {
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_ios',
    'fast_cli':False,
}

cfg = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]

net_connect = (ConnectHandler(**device1))
net_connect.find_prompt()
print("*" * 80)
pretime = datetime.now()
output = net_connect.send_config_set(cfg)
posttime = datetime.now()
print("\nExecution time with fast_cli off: {}".format(posttime - pretime))
print('*' * 80)
print(output)
print('*' * 80)
net_connect.disconnect()
device1['fast_cli']=True
net_connect = (ConnectHandler(**device1))
pretime = datetime.now()
output = net_connect.send_config_set(cfg)
posttime = datetime.now()
print('*' * 80)
print("\nExecution time with fast_cli on: {}".format(posttime - pretime))
print(output)
print("#" * 80)
print('*' * 80)
print('Sending ping to Google')
pingoutput = net_connect.send_command('ping google.com')
if "!!" in pingoutput:
    print('Ping to Google was successful')
    print(pingoutput)
else:
    print('Ping to Google was unsuccessful')
    print(pingoutput)

net_connect.disconnect()

''' His code
import os
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

start_time = datetime.now()
device = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    # "fast_cli": True,
}

net_connect = ConnectHandler(**device)
cmds = ["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"]
output = net_connect.send_config_set(cmds)
print()
print("#" * 80)
print("CFG Change: ")
print(output)
print("#" * 80)
print()

ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping Successful:")
    print("\n\nPing Output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing Failed: {}\n\n".format(ping_output))
net_connect.disconnect()

end_time = datetime.now()
print("Total Execution Time: {}\n".format(end_time - start_time))

'''
