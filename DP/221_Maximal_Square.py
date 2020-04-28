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


### Dynamic Programming
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(cols)]for i in range(rows)]

        for i in range(1, rows):# caution: starts from 1
            for j in range(1, cols):# caution: starts from 1
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
        output = max(max(row) for row in dp)

        return output ** 2

### DP with Space complexity O(1)
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(0, rows):
            for j in range(0, cols):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = 0
                elif matrix[i][j] == '1':
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                else:
                    matrix[i][j] = 0
        output = max(max(row) for row in matrix)

        return output ** 2
