class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        dq = deque([(p, q)])
        while dq:
            p, q = dq.popleft()
            if not p and not q:
                pass
            else:
                if not p or not q or p.val != q.val:
                    return False
            if q:
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))

        return True
