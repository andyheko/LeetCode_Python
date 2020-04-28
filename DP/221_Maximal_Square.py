###Brute Force
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        current = 0
        maximum = 0
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    current = 1
                    go = 1
                    while i + current < rows and j + current < cols and go:
                        for k in range(i, i+current+1):
                            if matrix[k][j+current] == '0':
                                go = 0
                                break
                        for l in range(j, j+current+1):
                            if matrix[i+current][l] == '0':
                                go = 0
                                break
                        if go:
                            current += 1
                    if current > maximum:
                        maximum = current





class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m , n = len(matrix), len(matrix[0])
        dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0

        res = max(max(row) for row in dp)
        return res ** 2
