"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first, last = None, None # first and last Node for DLL

        def dfs(node):
            nonlocal first, last
            if node:
                # left
                dfs(node.left)
                # node
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                # right
                dfs(node.right)

        dfs(root)
        # close DLL
        last.right = first
        first.left = last
        return first
