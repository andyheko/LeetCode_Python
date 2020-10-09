# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # [2, 1, 5]
        # stack = [(0,2)] res = [0]
        # stack = [(0,2), (1,1)] res = [0, 0]
        # stack = [(2,5)] res = [5, 5, 0]

        stack = [] # store (indx, val)
        res = []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res

        # [2, 7, 4, 3, 5]
        # stack = [(0, 2)] res = [0]
        # stack = [] res = [7]
        # stack = [(1,7)] res = [7, 0]
        # stack = [(1,7), (2,4), (3,3)] res = [7,0,0,0]
        # stack = [(1,7), (4,5)] res = [7, 5, 5, 0]
