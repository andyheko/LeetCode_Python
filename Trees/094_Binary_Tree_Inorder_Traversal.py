'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.inorderhelper(root, output)
        return output
    def inorderhelper(self, root, output):
        if root != None:
            self.inorderhelper(root.left, output)
            output.append(root.val)
            self.inorderhelper(root.right, output)
