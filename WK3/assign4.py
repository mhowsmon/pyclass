#!/usr/bin/env python

import json
from pprint import pprint

with open("arista.json") as f:
   data = json.load(f)

new_dict = {}
arp_entries = data["ipV4Neighbors"]

for entries in arp_entries:
    mac = entries['hwAddress']
    ip = entries['address']
    new_dict[ip] = mac

print(new_dict)

''' had to look at his code to get mine to work. gotta get used to json!

his

import json
from pprint import pprint

filename = "arista_arp.json"
with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
arp_entries = arp_data["ipV4Neighbors"]
for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()
'''
