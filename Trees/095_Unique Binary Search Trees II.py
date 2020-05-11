# Definition for a binary tree node.
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.helper(1, n)

    def helper(self, start, end):
        if start > end:
            return [None] # for none element
        result = []
        for i in range(start, end+1): # pick up a root
            left_trees = self.helper(start, i-1) # all possible left subtrees
            right_trees = self.helper(i+1, end) # all possible right subtrees
            for j in left_trees:
                for k in right_trees:
                    current = TreeNode(i)
                    current.left = j
                    current.right = k
                    result.append(current)
        return result
