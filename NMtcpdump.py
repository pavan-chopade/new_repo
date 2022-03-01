#!usr/bin/env python3
from ipaddress import IPv4Address, IPv6Address, ip_address
from telnetlib import IP
import NMdhcpserver
from getmac import get_mac_address
from scapy.all import *
import csv
def ipv6_add():
    packets = rdpcap("tcpdump2")
    ip1 = packets[1]['IPv6'].src
    ip2 = packets[20]['IPv6'].src
    final_ipv6 = [ip1,ip2]
    print(final_ipv6)
    return (final_ipv6)

def mac(ipv6):
    #Storing the variable
    ip=ipv6
    #creating empty list for storing the ma address
    lis=[]
    #iterating over both the ipv6 addresses
    for ip1 in ip:
        mask= ip1.find("/")
        if mask != -1:
            ip1 = ip1[:mask] 
        splitmac = ip1.split(":")
        macs = []
        for i in splitmac[-4:]:
            while len(i) < 4:
                i = "0" + i
            macs.append(i[:2])
            macs.append(i[-2:])
        macs[0] = "%02x" % (int(macs[0], 16) ^ 2)
        del macs[4]
        del macs[3]
        d= ":".join(macs)
        lis.append(d)
    #Creating a file to save the mac addresses
    with open ('mac.txt', 'w') as file:
        for ipa in lis:
            file.write(f"{ipa}\n")
    return(lis)


if __name__ =='__main__':
    store = ipv6_add()
    a= mac(store)
    print (a)



    
    