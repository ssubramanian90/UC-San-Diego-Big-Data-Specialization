#!/usr/bin/env python
import sys

prev_word=None
running_total=0

for line in sys.stdin:
    line=line.strip()
    key_value=line.split("\t")
    curr_word=key_value[0]
    value_in=key_value[1]
    value_in=int(value_in) 
    if prev_word == curr_word:
       running_total+= value_in
    else:
       if prev_word:
	  print('%s\t%s'%(prev_word, running_total))
       running_total=value_in
       prev_word=curr_word

if prev_word == curr_word:
   print('%s\t%s'%(prev_word, running_total))
