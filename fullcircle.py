#!/usr/bin/python

import requests, socket, dns.resolver, dns.reversename, termcolor

ip = requests.get('http://ipaddr.be')
ip = ip.text.rstrip()
print("Checking"), termcolor.colored(ip, 'cyan', attrs=['bold']), ("for FCrDNS")

addr = str(dns.reversename.from_address(ip))
ptr = str(dns.resolver.query(addr,"PTR")[0])
print termcolor.colored('OK!', 'green', attrs=['bold']), (addr + " resolves to " + ptr)

a = str(dns.resolver.query(ptr, 'A')[0])
if a == ip:
	print termcolor.colored('Success!', 'green', attrs=['bold']), ("FCrDNS established: " + ptr + " resolves to " + a)
else:
	print ("Failure! " + ptr + " resolves to " + a)