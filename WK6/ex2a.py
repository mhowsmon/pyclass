#!/usr/bin/env python

import pyeapi
from getpass import getpass
import yaml
from pprint import pprint

def yaml_load_devices(filename="arista_devices.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")

#enable = getpass("Enable: ")
devices = yaml_load_devices()
devices['arista4']['password'] = getpass()
print(devices['arista4'])

connection = pyeapi.client.connect(**devices['arista4'])
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")
arp_list = output[0]["result"]["ipV4Neighbors"]

for arp_entry in arp_list:
    mac_address = arp_entry["hwAddress"]
    ip_address = arp_entry["address"]
    print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))



''' His code
import os
import pyeapi
import yaml
from getpass import getpass


def yaml_load_devices(filename="arista_devices.yml"):
    with open(filename, "r") as f:
        return yaml.safe_load(f)
    raise ValueError("Reading YAML file failed")


def main():

    devices = yaml_load_devices()
    password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip arp")

        print()
        print("-" * 40)
        arp_list = output[0]["result"]["ipV4Neighbors"]
        for arp_entry in arp_list:
            mac_address = arp_entry["hwAddress"]
            ip_address = arp_entry["address"]
            print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))
        print("-" * 40)
        print()


if __name__ == "__main__":
    main()

'''
