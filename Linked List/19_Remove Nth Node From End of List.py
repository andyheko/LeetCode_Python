# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first = head
        counter = 0
        while first:
            counter += 1
            first = first.next
        counter -= n
        first = dummy
        while counter > 0:
            counter -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n+1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next
