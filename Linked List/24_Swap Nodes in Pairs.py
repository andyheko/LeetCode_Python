# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        prevNode = dummy
        while head and head.next:
            # define firstNode and secondNode
            firstNode = head
            secondNode = head.next
            #swap
            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            # Reinitialize prevNode and head
            prevNode = firstNode
            head = firstNode.next

        return dummy.next
