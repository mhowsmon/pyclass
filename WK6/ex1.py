#!/usr/bin/env python

import pyeapi
from getpass import getpass
from pprint import pprint

connection = pyeapi.client.connect(
    transport = "https", 
    host = "arista3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    port = "443",
)

#enable = getpass("Enable: ")
device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")
arp_list = output[0]["result"]["ipV4Neighbors"]

for arp_entry in arp_list:
    mac_address = arp_entry["hwAddress"]
    ip_address = arp_entry["address"]
    print("{:^15}{:^5}{:^15}".format(ip_address, "-->", mac_address))
