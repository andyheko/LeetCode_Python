# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tree = []
        def helper(node):
            if node:
                helper(node.left)
                tree.append(node.val)
                helper(node.right)
        helper(root)
        for i in range(1, len(tree)):
            if tree[i-1] >= tree[i]:
                return False
        return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return check(node.left, lower, node.val) and check(node.right, node.val, upper)

        return check(root, float('-inf'), float('inf'))

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        dq = deque([(root, float('-inf'), float('inf'))])
        while dq:
            root, lower, upper = dq.popleft()
            if not root:
                continue
            if not lower < root.val < upper:
                return False

            dq.append((root.left, lower, root.val))
            dq.append((root.right, root.val, upper))

        return True
