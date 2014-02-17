#!/usr/bin/env python

i = 1
sum = 0

while i < 1000001:
  
	binary = bin(i)[2:]
    
  	if str(i) == str(i)[::-1] and binary == binary[::-1]:
    		sum += i
		print i, binary
    
	i += 2
print sum
