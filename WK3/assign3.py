#!/usr/bin/env python

import json
from pprint import pprint

with open("input.json") as f:
   data = json.load(f)
ipv4list = []
ipv6list = []

for interface in data:
   for iptype in data[interface]:
      if iptype == 'ipv4':
         for ipaddress in data[interface][iptype]:
           ipaddr = ipaddress
           for mask in data[interface][iptype][ipaddress]:
             prefix = data[interface][iptype][ipaddress][mask]
           ipv4list.append(ipaddr + "/" + str(prefix))
      elif iptype == 'ipv6':
         for ipaddress in data[interface][iptype]:
           ipaddr = ipaddress
           for mask in data[interface][iptype][ipaddress]:
             prefix = data[interface][iptype][ipaddress][mask]
           ipv6list.append(ipaddr + "/" + str(prefix))
      else:
         print("something went wrong")
print()
pprint(ipv4list)
print()
pprint(ipv6list)

''' His code
#!/usr/bin/env python

import json

filename = "input.json"
with open(filename) as f:
    nxos_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf, ipaddr_dict in nxos_data.items():
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        for ip_addr, prefix_dict in addr_info.items():
            prefix_length = prefix_dict["prefix_length"]
            if ipv4_or_ipv6 == "ipv4":
                ipv4_list.append("{}/{}".format(ip_addr, prefix_length))
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_length))

'''
