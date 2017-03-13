#!/usr/bin/python
import re

slovo = 'madam m adam'
slovo2 = re.sub(r'\s', '', slovo)
print slovo2

a = slovo2[::-1]
if slovo2 == a:
    print ("it's polidrome")
else:
    print ("it's not polidrome")