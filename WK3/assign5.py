#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler
from pprint import pprint

with open("/home/mhowsmon/.netmiko.yml") as f:
   data = yaml.load(f)

device1 = data['cisco3']

net_connect = (ConnectHandler(**device1))

print(net_connect.find_prompt())
net_connect.disconnect()
