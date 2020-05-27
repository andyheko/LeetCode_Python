class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: # base case
            return 1
        if n < 0: # if n goes negative
            return 1 / self.myPow(x, -n)
        if n % 2: # n is odd
            return x * self.myPow(x, n-1)
        else: # n is even
            return self.myPow(x*x, n/2)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: # base case
            return 1
        if n < 0: # if n goes negative
            return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        if n % 2: # n is odd
            return x * half * half
        else: # n is even
            return half * half
