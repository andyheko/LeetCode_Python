"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur, stack = head, []
        while cur:
            if cur.child: # if cur node has child
                if cur.next: # stack cur node's next
                    stack.append(cur.next)
                # link cur to cur.child
                cur.next, cur.child.prev, cur.child = cur.child, cur, None

            if not cur.next and len(stack): # no next pointer and has stack
                tmp = stack.pop()
                # link cur to tmp
                cur.next, tmp.prev = tmp, cur
            cur = cur.next
        return head
