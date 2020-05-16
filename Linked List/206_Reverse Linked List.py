# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        dummy = ListNode(-1)
        prev = dummy
        while stack:
            prev.next = ListNode(stack.pop())
            prev = prev.next

        return dummy.next
# iteration 1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev
# iteration 2
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
# recursion
