#!/usr/bin/env python
import sys

lst=list()
for line in sys.stdin:
    line=line.strip()
    key_value=line.split('\t')
    key=key_value[0]
    value=key_value[1]
    if value=="ABC":
       lst.append(key)
     

    






