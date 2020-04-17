# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1

        output = ListNode(-1)
        current = output
        add = 0
        sum = 0

        while l1 or l2:
            if l1:
                sum += l1.val
            if l2:
                sum += l2.val

            if sum + add >= 10:
                current.next = ListNode((sum + add) % 10)
                add = 1
            else:
                current.next = ListNode(sum + add)
                add = 0
            sum = 0
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
            if add == 1:
                current.next = ListNode(1)
        return output.next
