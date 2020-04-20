# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        i = 1
        node = TreeNode(preorder[0])
        while i < len(preorder) and preorder[i] < node.val:
            i+=1
        node.left = self.bstFromPreorder(preorder[1:i])
        node.right = self.bstFromPreorder(preorder[i:])
        return node
