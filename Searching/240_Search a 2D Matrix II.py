class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        def binary_search(matrix, target, start, vertical):
            lo = start
            hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1
            while hi >= lo:
                mid = (lo + hi) // 2
                if vertical: # search a column
                    if matrix[start][mid] == target:
                        return True
                    elif matrix[start][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else: # search a row
                    if matrix[mid][start] == target:
                        return True
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
        for i in range(min(len(matrix), len(matrix[0]))): # iterate matrix diagonals
            vertical_search = binary_search(matrix, target, i, True)
            horizontal_search = binary_search(matrix, target, i, False)
            if vertical_search or horizontal_search:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        columns = len(matrix[0])

        row = rows - 1
        col = 0

        while col < columns and row >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False
