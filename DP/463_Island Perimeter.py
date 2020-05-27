class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 4
                    if i < len(grid) - 1 and grid[i+1][j] == 1: # make sure the rightest within limit, caution with the order between 'and'
                        count -= 2
                    if j < len(grid[0]) - 1 and grid[i][j+1] == 1: # make sure the bottom within limit, caution with the order between 'and'
                        count -= 2
        return count
