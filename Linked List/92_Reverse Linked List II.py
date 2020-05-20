# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        if m == n:
            return head
        # consider linked list as D,A[1],A[2]...
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        # move m-1 nodes, move prev to A[m-1]
        for _ in range(m-1):
            prev = prev.next

        # reverse from m to n, reverse m-n+1 nodes
        cur = prev.next
        reverse = None
        for _ in range(n-m+1):
            cur.next, reverse, cur = reverse, cur, cur.next
        # now the situation is
        # [dummy .... prev] [prev.next<-,..., <-reverse] [cur .....]
        prev.next.next = cur # link m with n+1
        prev.next = reverse # linke m-1 with n
        # now the situation is
        # [dummy .... prev, reverse,..., prev.next, cur .....]
        return dummy.next
