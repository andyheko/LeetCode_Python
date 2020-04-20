class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0: # skip the top left corner
                    continue
                elif r == 0: # for top elements
                    grid[r][c] = grid[r][c] + grid[r][c-1]
                elif c == 0: # for left elements
                    grid[r][c] = grid[r][c] + grid[r-1][c]
                else: # for other elememts
                    grid[r][c] = grid[r][c] + min(grid[r-1][c], grid[r][c-1])
        return grid[row-1][col-1]
