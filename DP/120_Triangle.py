### Top Down Solution
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        for i in range(1, len(triangle)): # skip the row 0
            for j in range(len(triangle[i])):
                if j == 0: # for every first element in row
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1: # for every last element in row
                    triangle[i][j] += triangle[i-1][j-1]
                else: # for others
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
### Buttom Up Solution
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        row = len(triangle)
        for i in range(row-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
