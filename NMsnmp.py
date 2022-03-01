#!usr/bin/env python3
from easysnmp import Session
from easysnmp import snmp_get, snmp_set, snmp_walk
from json import JSONEncoder
import json

session =  Session (hostname='198.51.100.1', community='netman@123', version=2)
int_oid = ['1.3.6.1.2.1.2.2.1.8.1', '1.3.6.1.2.1.2.2.1.8.3' ]
for i in int_oid:
    k=str(session.get(i))
    new_k= k.split()
    for i in new_k:
        if i == "value='1'":
            status = {"R4":{"int fa0/0":{f"Status: up"}}}
            print (status)
        elif i == "value='2'":
            status = {"R4":{"int fa1/0":{f"Status: down"}}}
            print (status)

l= str(session.walk('1.3.6.1.2.1.4.20.1.1'))
new_l=l.split()
for i in new_l:
    if i=="value='198.51.100.1'":
        add=i.split("=")
        address= {"R4":{f"ip add: {add[1]}":{"int fa0/0":{f"Status: up"}}}}
        print(address)

session =  Session (hostname='198.51.101.10', community='netman@123', version=2)
int_oid = ['1.3.6.1.2.1.2.2.1.8.1', '1.3.6.1.2.1.2.2.1.8.3' ]
for i in int_oid:
    k=str(session.get(i))
    new_k= k.split()
    for i in new_k:
        if i == "value='1'":
            status = {"R2":{"int fa0/0":{f"Status: up"}}}
            print (status)
        elif i == "value='2'":
            status = {"R2":{"int fa1/0":{f"Status: down"}}}
            print (status)

l= str(session.walk('1.3.6.1.2.1.4.20.1.1'))
new_l=l.split()
for i in new_l:
    if i=="value='198.51.100.1'":
        add=i.split("=")
        address= {"R2":{f"ip add: {add[1]}":{"int fa0/0":{f"Status: up"}}}}
        print(address)

session =  Session (hostname='198.51.101.11', community='netman@123', version=2)
int_oid = ['1.3.6.1.2.1.2.2.1.8.1', '1.3.6.1.2.1.2.2.1.8.3' ]
for i in int_oid:
    k=str(session.get(i))
    new_k= k.split()
    for i in new_k:
        if i == "value='1'":
            status = {"R3":{"int fa0/0":{f"Status: up"}}}
            print (status)
        elif i == "value='2'":
            status = {"R3":{"int fa1/0":{f"Status: down"}}}
            print (status)

l= str(session.walk('1.3.6.1.2.1.4.20.1.1'))
new_l=l.split()
for i in new_l:
    if i=="value='198.51.100.1'":
        add=i.split("=")
        address= {"R3":{f"ip add: {add[1]}":{"int fa0/0":{f"Status: up"}}}}
        print(address)

m= (session.walk('1.3.6.1.2.1.4.34.1.5.2.16'))
print (m)

cpu = str(session.get('1.3.6.1.4.1.9.2.1.58.0'))
print(cpu)

class setEncoder(json.JSONEncoder):
    def default(self, obj):
        print(JSONEncoder)
        return list(obj)

final_data = json.dumps(address, indent=4, cls=setEncoder)
print(final_data)

int_status= json.dumps(status, indent=4, cls=setEncoder)
print(int_status)

with open ("finadata.txt","a") as f1:
    f1.write(final_data)
    f1.write(int_status)

    