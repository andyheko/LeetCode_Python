# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # two pointer
        ha = headA
        hb = headB

        while ha != hb:
            if ha == None:# if either pointer hits the end, switch head and continue the second traversal
                ha = headB
            else:# if not hit the end, just move on to next
                ha = ha.next

            if hb == None:
                hb = headA
            else:
                hb = hb.next

        return ha # only 2 ways to get out of the loop, they meet or the both hit the end=None
