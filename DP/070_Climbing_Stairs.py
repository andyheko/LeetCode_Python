class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def helper(n):
            if n <= 2:
                return n

            if not n in memo:
                memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)

class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        first = 1
        second = 2
        for i in range(2,n):
            third = first + second
            first = second
            second = third
        return second
