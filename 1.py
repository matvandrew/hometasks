#!/usr/bin/python
list_key = ['key1', 'key2', 'key3', 'key4', 'key5'];
#print list_key
list_value = [1,2,3];
#print list_value

def function(list_key, list_value):
    global dict0
    dict0 = {}
    for i in range(len(list_key)):
        if i < len(list_value):
            dict0[list_key[i]] = [list_value[i]]
        else:
            dict0[list_key[i]] = 'None'
    return dict0

function(list_key, list_value)
print dict0