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

''' His code
import yaml
from os import path
from netmiko import ConnectHandler


home_dir = path.expanduser("~")
filename = path.join(home_dir, ".netmiko.yml")

with open(filename) as f:
    yaml_out = yaml.safe_load(f)

cisco3 = yaml_out["cisco3"]
net_connect = ConnectHandler(**cisco3)

print()
print(net_connect.find_prompt())
print()

'''
