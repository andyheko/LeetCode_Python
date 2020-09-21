class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list) # {pre: curr}
        indegree = defaultdict(int) # {curr: # of indegree}
        for curr, pre in prerequisites:
            adj_list[pre].append(curr)
            indegree[curr] += 1

        # queue for nodes having 0 in-degree
        queue = deque([k for k in range(numCourses) if k not in indegree])

        ans = []
        while queue:
            # pop first node with 0 in-degree
            vertex = queue.popleft()
            ans.append(vertex)

            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1 # reduce in-degree for neighbors of vertex

                    # add neighbor to queue if in-degree == 0
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        return ans if len(ans) == numCourses else []
