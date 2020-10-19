# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def dfs(node, acc, path, ans):
            if node:
                path.append(node.val)
                acc += node.val
                if acc == sum and not node.left and not node.right: # reach sum & at leaf
                    ans.append(list(path)) #### "list" important
                else:
                    dfs(node.left, acc, path, ans)
                    dfs(node.right, acc, path, ans)
                path.pop()### important, need to pop node once done process its subtrees

        ans = []
        dfs(root, 0, [], ans)
        return ans
