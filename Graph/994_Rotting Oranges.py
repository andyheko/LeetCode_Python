class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        minute_passes = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # start BFS rotting process
        while rotten and fresh_oranges > 0:
            minute_passes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions: # for 4 directions near rotten orange
                    rr, cc = r + dr, c + dc
                    if rows > rr >= 0 and cols > cc >= 0:
                        if grid[rr][cc] == 1: # if it is a fresh orange
                            grid[rr][cc] = 2
                            fresh_oranges -= 1
                            rotten.append((rr, cc))

        return minute_passes if fresh_oranges == 0 else -1
