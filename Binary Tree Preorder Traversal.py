# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        ans = []
        top = root
        stack = []
        while top or stack:
            if top is None:
                top = stack.pop()
            ans.append(top.val)
            if top.right:
                stack.append(top.right)
            top = top.left
        return ans      
