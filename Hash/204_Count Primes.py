class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: # for n == 1 or 2, return 0
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1): # avoid repeatedly calling
            if primes[i]:
                for j in range(i * i, n, i): # mark oof mutiples of prime i
                    primes[j] = False
        return sum(primes)
