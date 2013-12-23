#!/bin/bash

# define some colors
cyan='\033[1;36m'
# a really stupid comment
green='\033[1;32m'
red='\033[1;31m'
nc='\033[0m'

if [ -n "$1" ]
	then ip=$1; echo -e Checking ${cyan}$ip${nc} for FCrDNS
	else ip=`curl -s ipaddr.be`; echo -e $HOSTNAME\'s likely mailing ip: ${cyan}$ip${nc}; echo
fi

ptr=`dig +short -x $ip`
echo -e The rDNS record for $ip is ${cyan}$ptr${nc}; echo

arecord=`dig +short a $ptr`
echo -e $ptr resolves to ${cyan}$arecord${nc}; echo

if [ $arecord = $ip ]
	then echo -e "${green}FCrDNS established! Hooray!"
	else echo -e "${red}FCrDNS checks failed!"
fi
