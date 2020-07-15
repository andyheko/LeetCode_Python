# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val

        if p_val > root.val and q_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < root.val and q_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val

        node = root

        while node:
            if p_val > node.val and q_val > node.val:
                node = node.right
            elif p_val < node.val and q_val < node.val:
                node = node.left
            else:
                return node
