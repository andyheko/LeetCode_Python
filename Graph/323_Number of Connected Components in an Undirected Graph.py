class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i):
            if visited[i]:
                return
            visited[i] = 1
            for node in adjList[i]:
                dfs(node)

        visited = [0] * n # if visited, 0 => 1
        adjList = defaultdict(list) # adjecent list, {node:[node,node.....],....}
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {x:[] for x in range(n)} # adjecent list, {node:[node,node.....],....}
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)

        count = 0
        for i in range(n):
            queue = [i]
            if i in adjList:
                count += 1
                for node in queue:
                    if node in adjList:
                        queue += adjList[node]
                        del adjList[node]
        return count
