# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x: # assign the before list
                before.next = head
                before = before.next
            else: # assign the after list
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next # combine before list to after list
        return before_head.next
