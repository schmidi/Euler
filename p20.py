#!/usr/bin/env python

def factorial(n):
  
  assert n > 1
  
  result = 1
  
  for i in range(2, n+1):
    result *= i
    
  return result


result = factorial(100)
i = 0
sum = 0
while i < len(str(result)):
  sum += int(str(result)[i])
  i += 1
print sum
