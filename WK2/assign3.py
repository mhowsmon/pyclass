#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from netmiko import ConnectHandler

device1 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_ios',
}

net_connect = (ConnectHandler(**device1))
net_connect.find_prompt()
output = net_connect.send_command("show version", use_textfsm=True)
print(output)
print(type(output))
print('*' * 80)
output = net_connect.send_command("show lldp neighbors detail", use_textfsm=True)
print(output)
print(type(output))
print("#" * 80)
print("Local Interface of LLDP Neighbor:", output[0]['local_interface'], "Neighbor Interface:", output[0]['neighbor_port_id'])
net_connect.disconnect()
