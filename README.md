# port25-utils

Assortment of scripts to help linux administrators troubleshoot email issues.

* * *

## fullcircle.py

Just like the bash script but sexier.  

### pip modules
- requests
- dns
- termcolor

### Todo
- Accept multiple ips & CIDRs as arguments to check. 
- Specify nameserver
- Email a pretty report

## fullcircle.sh

Portable bash script using curl & dig to Check if an ip has properly established [FCrDNS](http://en.wikipedia.org/wiki/Forward-confirmed_reverse_DNS "Forward-confirmed reverse DNS").

## mail-test.php

Send a test email message using php's mail function. 