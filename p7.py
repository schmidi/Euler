#!/usr/bin/env python

import random


def isPrime(n, k=4):
    """Returns whether a value is prime or not using the miller-rabin test.

     Args:
         n: the number to test for prime
         k: accuracy of the result
     Returns:
         a boolean
     """
    assert n >= 2
    assert k > 0

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    def __tryComposite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(k):
        a = random.randrange(2, n)
        if __tryComposite(a):
            return False
    return True


counter = 1
value = 2
i = 3

while counter < 10001:
    if isPrime(i):
        value = i
        counter += 1
    i += 1
print counter, value



