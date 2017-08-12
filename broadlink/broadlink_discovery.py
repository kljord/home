#!/usr/bin/python

import broadlink
import time
import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='@');
parser.add_argument("--timeout", type=int, default=5, help="timeout to wait for receiving discovery responses")
args = parser.parse_args()

print "discover"
devices = broadlink.discover(timeout=args.timeout)
#print devices
for device in devices:
    if device.auth():
        print "###########################################"
#       print device
        print device.type
        print "# broadlink_cli --type 0x2712 --host {} --mac {}".format(device.host[0], ''.join(format(x, '02x') for x in device.mac))
        print "Device file data (to be used with --device @filename in broadlink_cli) : "
        print "0x2712 {} {}".format(device.host[0], ''.join(format(x, '02x') for x in device.mac))
        print "temperature = {}".format(device.check_temperature())
        print ""
    else:
        print "Error authenticating with device : {}".format(device.host)