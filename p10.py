#!/usr/bin/env python

from primes import Primes


result = 2

for i in range(3, 2 * 10**6):
    if Primes().isPrime(i):
        result += i
print result



