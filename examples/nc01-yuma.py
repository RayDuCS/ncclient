#! /usr/bin/env python2.6
#
# Connect to the NETCONF server passed on the command line and
# display their capabilities. This script and the following scripts
# all assume that the user calling the script is known by the server
# and that suitable SSH keys are in place. For brevity and clarity
# of the examples, we omit proper exception handling.
#
# $ ./nc01.py broccoli

import sys, os, warnings, logging
warnings.simplefilter("ignore", DeprecationWarning)
from ncclient import manager

def demo(host, user):
    with manager.connect(host=host, port=830, username='vagrant',
        password='vagrant') as m:
        for c in m.server_capabilities:
            print c

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    demo(sys.argv[1], os.getenv("USER"))
