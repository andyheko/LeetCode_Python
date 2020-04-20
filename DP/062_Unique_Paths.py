class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1

        for c in range(1, m):
            for r in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[n-1][m-1]

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[(0,0)] = 1

        def helper(i, j, m, n, dp):
            if i<0 or j<0 or i>=m or j >=n:
                return 0
            elif (i, j) in dp:
                return dp[(i, j)]
            else:
                dp[(i, j)] = helper(i-1, j, m, n, dp) + helper(i, j-1, m, n, dp)
                return dp[(i, j)]

        return helper(m-1, n-1, m, n, dp)
