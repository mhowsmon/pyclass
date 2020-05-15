#!/usr/bin/env python
from __future__ import unicode_literals, print_function
from netmiko import ConnectHandler
from datetime import datetime

device1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
}

device2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos'
}

devicelst = []
devicelst.append(device1)
devicelst.append(device2)

for device in devicelst:
    net_connect = (ConnectHandler(**device))
    net_connect.find_prompt()
    output = net_connect.send_config_from_file(config_file='vlan_add.txt')
    print(output)
    output = net_connect.save_config()
    print(output)
    net_connect.disconnect()

''' his code
import os
from netmiko import ConnectHandler
from getpass import getpass


def display_output(output):
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()


if __name__ == "__main__":
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
    nxos1 = {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    }
    nxos2 = {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    }

    for device in (nxos1, nxos2):
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file("vlans.txt")
        display_output(output)
        net_connect.save_config()
        net_connect.disconnect()
'''
