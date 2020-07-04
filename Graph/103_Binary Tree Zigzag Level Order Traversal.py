# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        level_q = deque()
        node_q = deque([root, None]) # * need None to mark end of level
        order_left = True # from left to right, FIFO
        while node_q:
            node = node_q.popleft()
            if node:
                if order_left == True: # FIFO
                    level_q.append(node.val)
                else: # FILO
                    level_q.appendleft(node.val)
                # BFS
                if node.left:
                    node_q.append(node.left)
                if node.right:
                    node_q.append(node.right)
            else: # finish one BFS level
                ans.append(level_q)
                if node_q: # if there is next level
                    node_q.append(None) # mark the end of next level
                # prepare next level
                level_q = deque()
                order_left = not order_left
        return ans

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = [] # [[node.val, .....], [], []...]
        def dfs(node, level):
            if level >= len(ans):
                ans.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    ans[level].append(node.val)
                else:
                    ans[level].appendleft(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return ans
