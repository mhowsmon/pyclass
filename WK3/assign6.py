#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse
from pprint import pprint

with open("/home/mhowsmon/.netmiko.yml") as f:
   data = yaml.load(f)

cisco4 = data['cisco4']

net_connect = (ConnectHandler(**cisco4))

command = "show run"

output = net_connect.send_command(command)
cisco_obj = CiscoConfParse(output.splitlines())
match = cisco_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

for intf in match:
    print("Interface Line: {}".format(intf.text))
    print()
    ipaddr = intf.re_search_children(r"ip address")[0].text    
    print("IP Address Line: {}".format(ipaddr))

''' his code

import yaml
from os import path
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse


if __name__ == "__main__":
    home_dir = path.expanduser("~")
    filename = path.join(home_dir, ".netmiko.yml")

    with open(filename) as f:
        yaml_out = yaml.safe_load(f)

    device = yaml_out["cisco4"]
    net_connect = ConnectHandler(**device)
    show_run = net_connect.send_command("show run")

    # When feeding config directly - CiscoConfParse requires a list
    cisco_cfg = CiscoConfParse(show_run.splitlines())
    interfaces = cisco_cfg.find_objects_w_child(
        parentspec=r"^interface", childspec=r"^\s+ip address"
    )

    print()
    for intf in interfaces:
        print("Interface Line: {}".format(intf.text))
        ip_address = intf.re_search_children(r"ip address")[0].text
        print("IP Address Line: {}".format(ip_address))
        print()
    print()

'''
