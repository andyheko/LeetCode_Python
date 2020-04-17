class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(i, j):
            if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
                if grid[i][j] == '1':
                    grid[i][j] = '0'

                    dfs(i-1, j)
                    dfs(i+1, j)
                    dfs(i, j-1)
                    dfs(i, j+1)
                    return True
            return False

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i,j):
                    count += 1
        return count

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # flip card from 1 to 0
            grid[i][j] = '0'
            # recursive function all adjacent cards
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if encounter '1', count +=1, meanwhile fip all adjacent 1 to 0
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count            
