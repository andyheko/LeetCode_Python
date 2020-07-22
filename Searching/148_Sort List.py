# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def getSize(head):
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def split(head, step):
            i = 1
            while i < step and head:
                head = head.next
                i += 1
            if not head:
                return None
            # disconnect
            temp, head.next = head.next, None
            return temp

        def merge(l, r, head):
            curr = head
            while l and r:
                if l.val < r.val:
                    curr.next, l = l, l.next
                else:
                    curr.next, r = r, r.next
                curr = curr.next
            curr.next = l if l else r
            while curr.next:
                curr = curr.next
            return curr

        size = getSize(head)
        bs = 1
        dummy = ListNode(-1)
        dummy.next = head
        l = r = tail = None
        while bs < size:
            curr = dummy.next
            tail = dummy
            while curr:
                l = curr
                r =  split(l, bs)
                curr = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next
