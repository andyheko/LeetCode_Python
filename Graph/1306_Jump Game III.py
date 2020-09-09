class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        bfs = deque()
        bfs.append(start)
        while bfs:
            node = bfs.popleft()
            if arr[node] == 0:
                return True
            # check available next steps
            if arr[node] > 0:
                for next in [node + arr[node], node - arr[node]]:
                    if 0 <= next < len(arr):
                        bfs.append(next)
                arr[node] = -arr[node] # mark as visited

        return False
