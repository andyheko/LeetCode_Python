class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(u, v): # traverse
            if u not in seen:
                seen.add(u)
                print(seen)
                if u == v: # neighbor == v
                    return True
                for neighbor in graph[u]:
                    if dfs(neighbor, v): # keep recursive to find neighbor == v
                        return True
                return False # no neighbor == v

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v): # only run dfs when u, v both in graph
                return u, v
            graph[u].add(v)
            graph[v].add(u)
            print(graph)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)

        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for x, y in edges:
            if not union(x - 1, y - 1):
                return [x, y]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * (len(edges) + 1)  # idx = node number, 1~N

        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV:
                return True
            parent[rootU] = rootV
            return False

        for u, v in edges:
            if union(u, v):
                return [u, v]
