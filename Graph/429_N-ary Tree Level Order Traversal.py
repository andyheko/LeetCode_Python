"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        bfs = deque()
        bfs.append(root)
        while bfs:
            level = []
            size = len(bfs)
            for _ in range(size):
                node = bfs.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    bfs.append(child)
            if level:
                res.append(level)
        return res
