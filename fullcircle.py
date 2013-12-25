#!/usr/bin/python

import requests, socket

ip = requests.get('http://ipaddr.be')
ip = ip.text.rstrip()
print("Checking " + ip + " for FCrDNS")

from dns import resolver,reversename
addr = reversename.from_address(ip)
ptr = str(resolver.query(addr,"PTR")[0])
print ("PTR record for " + ip + " is " + (ptr))

from dns import resolver
a = str(resolver.query((ptr), 'A')[0])

if a == ip:
	print ("Success! FCrDNS established: " + ptr + " resolves to " + a)
else:
	print ("Failure! " + ptr + " resolves to " + a)