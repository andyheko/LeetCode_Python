# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            curr_level = queue
            queue = deque()

            while curr_level:
                node = curr_level.popleft()
                #add child nodes in queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # finish current level, last element is rightmost
            ans.append(node.val)
        return ans

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length -1: # if it's the last element(rightmost)
                    ans.append(node.val)
                #add child nodes in queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        ans = []

        def dfs(node, level):
            if node:
                if level == len(ans):
                    ans.append(node.val)
                # important order*
                dfs(node.right, level+1)
                dfs(node.left, level+1)

        dfs(root, 0)
        return ans
