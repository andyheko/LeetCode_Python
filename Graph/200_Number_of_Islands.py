class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

        R = len(grid)
        C = len(grid[0])
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R = len(grid)
        C = len(grid[0])
        count = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    bfs = deque()
                    bfs.append((r,c))
                    while bfs:
                        rr, cc = bfs.popleft()
                        if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == '1':
                            grid[rr][cc] = '0'
                            bfs.append((rr-1, cc))
                            bfs.append((rr+1, cc))
                            bfs.append((rr, cc-1))
                            bfs.append((rr, cc+1))
        return count
