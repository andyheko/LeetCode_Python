# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes_list = []
        head = curr = ListNode(-1)
        for l in lists:
            while l:
                nodes_list.append(l.val)
                l = l.next
        for node in sorted(nodes_list):
            curr.next = ListNode(node)
            curr = curr.next
        return head.next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge2Lists(l, r)
    def merge2Lists(self, l1, l2):
        head = curr = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return head.next
