# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        ans = []

        def helper(node, level):
            if level == len(ans):
                ans.append([])
            ans[level].append(node.val)

            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return ans

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None

        dq = deque([root])
        ans = []
        level = 0
        while dq:
            ans.append([])
            level_len = len(dq) # number of elements in current level
            for i in range(level_len):
                node = dq.popleft()
                ans[level].append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            # go next leve
            level += 1
        return ans
