# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list) # store the ans. as [column, [node.value...], ...]
        queue = deque([(root, 0)]) # BFS: store (node, column) in a list
        while queue:
            node, column = queue.popleft()
            if node:
                columnTable[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        return [columnTable[x] for x in sorted(columnTable.keys())]

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list) # store the ans. as [column, [node.value...], ...]
        max_col = min_col = 0
        queue = deque([(root, 0)]) # BFS: store (node, column) in a list
        while queue:
            node, column = queue.popleft()
            if node:
                min_col = min(min_col, column)
                max_col = max(max_col, column)
                columnTable[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        return [columnTable[x] for x in range(min_col, max_col+1)]
