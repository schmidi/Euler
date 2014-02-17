#!/usr/bin/env python

import random
import struct
import binascii
import os


class Primes:

    def isPrime(self, n, k=4):
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

    def generateRandomPrime(self, bitLength=1024):

        nBytes, nBit = divmod(bitLength, 8)

        while True:
            probablePrime = os.urandom(nBytes)
            # fill remaining bits (if any)
            if nBit > 0:
                randomBits = ord(os.urandom(1))
                randomBits >>= (8 - nBit)
                probablePrime += struct.pack("B", randomBits)
            probablePrime = int(binascii.hexlify(probablePrime), 16)
            # Make sure value is big enough
            probablePrime |= 1 << (bitLength - 1)
            # Ensure that the value is odd
            probablePrime |= 1

            if self.isPrime(probablePrime):
                return probablePrime