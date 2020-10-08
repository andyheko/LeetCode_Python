# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val: # imporant!!!
                    cur = cur.next
                cur = cur.next
                pre.next = cur ### imporant!!!
            else:
                pre = pre.next
                cur = cur.next

        return dummy.next
