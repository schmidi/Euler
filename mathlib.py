from primes import Primes


class MathLib():

    primes = Primes()

    def factorize(self, n, list, checkPrime=2):

        if self.primes.isPrime(n):
            list.append(n)
            return

        if n % checkPrime == 0:
            list.append(checkPrime)
            self.factorize(n / checkPrime, list, checkPrime)
        else:
            checkPrime += 1 if checkPrime == 2 else 2
            while not self.primes.isPrime(checkPrime):
                checkPrime += 2

            self.factorize(n, list, checkPrime)
