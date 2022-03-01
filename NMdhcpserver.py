#!usr/bin/env python3
# from ipaddress import ip_address
# from subprocess import list2cmdline
from netmiko import ConnectHandler
import csv

def main() :
    #opening a file containing the device info
    with open('sshinfo.csv', 'r') as input:
        reader = csv.DictReader(input)
        #Creating a list to store the dictionary
        list = []
        for rows in reader:
            list.append(rows)
        #Creating an ipset of the IPs from the list
        ipset = []
        for i in list:
            newlist=(str(i['ip']))
            ipset.append(newlist)
    #creating an empty list to store the client identifier
    client_id=[] 
    #getting the client identifier
    with open ('mac.txt') as f:
        for line in f:
            k = (line.split(':'))
            k.insert(0,'01')
            d="".join(k)
            id = f'{d[0:4]}.{d[4:8]}.{d[8:12]}.{d[12:14]}'
            client_id.append(id)
    print (client_id)
    #pushing the client identifier in the config file
    for id in client_id:
        with open('dhcpv4.txt', 'r') as file:
            data = file.readlines()
        data[15] = f'client-identifier {id}\n'
        with open('dhcpv4.txt', 'w') as file:
            file.writelines( data )   

#Establishing the connection
    for devices in list:
        connection_request=ConnectHandler(**devices)
        
        for list[0] in list:
            with open ('dhcpv4.txt') as f:
                lines=f.read().splitlines ()
            output=connection_request.send_config_set(lines)
            output =connection_request.send_command("sh ip dhcp binding")
            print(output) 
            
if __name__ == '__main__':
    main ()