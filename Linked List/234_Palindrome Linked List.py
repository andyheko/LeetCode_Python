# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dict = []
        curr = head
        while curr:
            dict.append(curr.val)
            curr = curr.next
        return dict == dict[::-1]

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        first_half_end = self.end_of_first_half(head) # end of first half
        second_half_start = self.reverse(first_half_end.next)# reverse second half

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next
        first_half_end.next = self.reverse(second_position) # restore original linked list
        return result


    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        previous = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = previous
            previous = curr
            curr = next_node
        return previous
