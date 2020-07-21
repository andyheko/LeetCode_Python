class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            mid_element = matrix[mid // n][mid % n]
            if mid_element == target:
                return True
            elif target < mid_element:
                end = mid - 1
            else:
                start = mid + 1
        return False
