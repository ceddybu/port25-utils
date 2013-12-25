#!/bin/bash
set -e

# define colors
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
nc='\033[0m'

# check for first argument
if [ -n "$1" ]
	then ip=$1; echo -e Checking ${cyan}$ip${nc} for FCrDNS...; echo
	# curl the public ip
    else ip=`curl -s ipaddr.be`; echo -e $HOSTNAME\'s likely mailing ip is ${cyan}$ip${nc}; echo
fi

ptr=`dig +short -x $ip`
if [ -n "$ptr" ]
    then echo -e ${green}OK!${nc} The PTR record for $ip is ${cyan}$ptr${nc}; echo
    else echo -e ${red}Fail! PTR lookup failed!${nc}; exit
fi

a=`dig +short a $ptr`
if [ $a = $ip ]
	then echo -e "${green}OK!${nc} $ptr resolves to ${cyan}$a${nc}\n\n${green}FCrDNS established! Hooray!${nc}"
	else echo -e "${red}FCrDNS checks failed! $ptr resolves to ${cyan}$a${nc}"
fi