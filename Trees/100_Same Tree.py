# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        dq = deque([(p, q)])
        while dq:
            p, q = dq.popleft()
            if not p and not q:
                pass
            else:
                if not p or not q or p.val != q.val:
                    return False
            if q:
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))

        return True
