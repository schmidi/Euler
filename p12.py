#!/usr/bin/env python

maxCount = 10000
sum = 0
length = 0

i = 1

while length < 500:
    sum += i
    factors = list()
    j = 1
    limit = sum
    while j < limit:
        if sum % j == 0:
            factors.append(j)
            factors.append(sum / j)
        j += 1
        limit = sum / j

    length = len(factors)
    i += 1

print sum


