#!/usr/bin/env python3

# It takes the inventory yaml file as parameter and generates the hosts file,
# which should be copy to all kubernetes cluster node as /etc/hosts.
#
# The inventory file should be in the ansible playbook root directory,
# as inventory.yaml. The inventory file has to contain "domain" var for FQDN.
#

import sys
import yaml

if (len(sys.argv) > 1):
    inventory_file = sys.argv[1]
else:
    print(sys.argv[0]+' <inventory filename>')
    exit()

try:
    with open(inventory_file) as file:
        inventory = yaml.safe_load(file)
# A FullLoader is accessable only from PyYAML version 5.1
#    inventory = yaml.load(file, Loader=yaml.FullLoader)
except yaml.YAMLError as err:
    print('Can not able load the inventory file ('+inventory_file+')! '+err)
    exit()
except Exception as err:
    print('Can not able load the inventory file ('+inventory_file+')! '+err)
    exit()


for groupname, group in inventory['all']['children'].items():
    try:
        if group['hosts']:
            for hostname, data in group['hosts'].items():
                print(data['ansible_host']+' '+hostname+'.'+inventory['all']['vars']['domain']+' '+hostname)
    except KeyError:
        continue
exit()
