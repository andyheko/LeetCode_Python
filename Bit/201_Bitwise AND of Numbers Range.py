class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1 # m = m >> 1, move right, / 2
            n >>= 1 # n = n >> 1
            i += 1
        return n << i # move left, * 2
