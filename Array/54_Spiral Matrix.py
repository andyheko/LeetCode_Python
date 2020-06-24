class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        ans = []
        l, r, t, b = 0, C - 1, 0, R - 1

        while l <= r and t <= b:
            # move right
            for i in range(l, r+1):
                ans.append(matrix[t][i])
            t += 1

            # move down
            for i in range(t, b+1):
                ans.append(matrix[i][r])
            r -= 1

            # move left
            if t <= b: # double check if need to move left
                for i in range(r, l-1, -1):
                    ans.append(matrix[b][i])
                b -= 1

            # move up
            if l <= r: # double check if need to move up
                for i in range(b, t-1, -1):
                    ans.append(matrix[i][l])
                l += 1

        return ans
