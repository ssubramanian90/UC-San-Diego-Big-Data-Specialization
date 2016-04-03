#!/usr/bin/env python
import sys

for line in sys.stdin:
    line=line.strip()
    key_value=line.split(",")
    key_in= key_value[0].split(" ")
    key_in=''.join(key_in)
    value=key_value[1]
    print('%s\t%s'%(key_in, value))



