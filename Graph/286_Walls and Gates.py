class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return None
        R = len(rooms)
        C = len(rooms[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        bfs = deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    bfs.append((r,c))

        while bfs:
            rr, cc = bfs.popleft()
            for direction in directions:
                r, c = rr + direction[0], cc + direction[1]
                if r < 0 or c < 0 or r >= R or c >= C or rooms[r][c] != 2147483647:
                    continue
                rooms[r][c] = rooms[rr][cc] + 1
                bfs.append((r, c))
