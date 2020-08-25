# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        def findMiddle(head):
            prevP = None
            slowP = head
            fastP = head
            while fastP and fastP.next:
                prevP = slowP
                slowP = slowP.next
                fastP = fastP.next.next
            if prevP: # handle when slowP == head
                prevP.next = None
            return slowP # mid pointer

        mid = findMiddle(head)
        node = TreeNode(mid.val)
        if head == mid: # base case, only one element in linked list
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
