"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque([root])
        # iterate over each level
        while q:
            size = len(q)
            # iterate over nodes on current level
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
