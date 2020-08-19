"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {} # key: old node, value: new node

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited: # if node already visited
            return self.visited[node]
        else:
            new_node = Node(node.val, [])
            self.visited[node] = new_node
        # iterate through neighbors
        if node.neighbors:
            new_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return new_node

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
