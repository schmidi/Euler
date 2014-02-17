#!/usr/bin/env python

result = 2 ** 1000

i = 0
sum = 0
while i < len(str(result)):
  sum += int(str(result)[i])
  i += 1
print sum
