#!/usr/bin/python
from collections import Counter

log = open('access_log', 'r')

dict_ip = {}
for line in log:
    string = line.split(' -')
    ip = (string[0])
    #print (ip) # print all ip
    dict_ip[ip] = dict_ip.get(ip, 0)+1

log.close()

print(Counter(dict_ip).most_common(10))