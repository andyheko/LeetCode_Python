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
