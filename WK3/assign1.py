#!/usr/bin/env python
from pprint import pprint

with open('arp.txt') as f:
   data = f.readlines()

arplist = []

for line in data:
   if 'Internet' in line:
      arpdata = line.strip()
      _, ip_addr, _, mac_addr, _, intf = arpdata.split()
      mydict = {"mac_addr":mac_addr, "ip_addr":ip_addr, "interface":intf}
      arplist.append(mydict)
   else:
      continue
print()
pprint(arplist)
print()   
print(type(arplist))
print(len(arplist))
print(arplist[0]['mac_addr'])


''' His code

import re
from pprint import pprint

arp_data = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.220.88.1            67   0062.ec29.70fe  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.20           29   c89c.1dea.0eb6  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.22            -   a093.5141.b780  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.37          104   0001.00ff.0001  ARPA   GigabitEthernet0/0/0
Internet  10.220.88.38          161   0002.00ff.0001  ARPA   GigabitEthernet0/0/0
"""

arp_data = arp_data.strip()
arp_list = arp_data.splitlines()

processed_list = []
for arp_entry in arp_list:
    if re.search(r"^Protocol.*Interface", arp_entry):
        continue
    _, ip_addr, _, mac_addr, _, intf = arp_entry.split()
    arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}
    processed_list.append(arp_dict)

print()
pprint(processed_list)
print()

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security

'''
