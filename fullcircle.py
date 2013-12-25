#!/usr/local/bin/python

import requests, socket

ip = requests.get('http://ipaddr.be')
ip = ip.text.rstrip()
print("Checking " + ip + " for FCrDNS")

ptr = socket.gethostbyaddr(ip)
#try:
#  ptr
#except NameError:
#  print "There is a problem with the PTR record!"
#else:
print ("PTR for " + ip + " is " + (ptr)[0])

a = socket.gethostbyname(ptr[0])
if a == ip:
	print ("Success! FCrDNS established: " + ptr[0] + " resolves to " + a)
else:
	print ("Failure! " + ptr[0] + " resolves to " + a)