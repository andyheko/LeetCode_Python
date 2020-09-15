# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # dfs, transform tree into graph
        conn = collections.defaultdict(list)
        def connect(parent, child):
            # inorder traversal
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)

        # bfs, start from target
        bfs = collections.deque()
        bfs.append(target.val)
        seen = set([target.val])
        for i in range(K):
            size = len(bfs)
            for j in range(size):
                node = bfs.popleft()
                for k in conn[node]:
                    if k not in seen:
                        bfs.append(k)
                        seen.add(k)
        return list(bfs)
