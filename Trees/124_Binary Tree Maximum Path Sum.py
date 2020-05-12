# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_sum = float('-inf')

        def max_gain(node):
            nonlocal max_sum

            if not node:
                return 0
            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)
            # return max_gain for recursion if continue same path
            return node.val + max(left_gain, right_gain)

        max_gain(root) # start the recursion chain
        return max_sum
