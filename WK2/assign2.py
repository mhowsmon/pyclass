#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from datetime import datetime
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
    'global_delay_factor':2
}

net_connect = (ConnectHandler(**device1))
net_connect.find_prompt()
extime = datetime.now()
output = net_connect.send_command("show lldp neighbors detail")
endtime = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution time: {}".format(endtime - extime))
print()
extime = datetime.now()
output = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
endtime = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution time: {}".format(endtime - extime))
print()
net_connect.disconnect()
