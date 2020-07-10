# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False

            return helper(t1.right, t2.left) and helper(t1.left, t2.right)
        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        dp = deque([root, root])
        while dp:
            t1 = dp.popleft()
            t2 = dp.popleft()
            if not t1 and not t2:
                pass
            else:
                if not t1 or not t2 or t1.val != t2.val:
                    return False
            if t1:
                dp.append(t1.left)
                dp.append(t2.right)
                dp.append(t1.right)
                dp.append(t2.left)

        return True
