# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        tortoise = hare = head
        while True:
            if not hare or not hare.next:
                return None
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break


        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise
