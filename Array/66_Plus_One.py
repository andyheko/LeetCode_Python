'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        length = len(digits)
        output = []
        for i in digits:
            sum += i * (10**(length-1))
            length-=1
        sum+=1
        length2 = len(str(sum))
        for i in range(length2):
            output.append(sum//10**(length2-1))
            sum -= sum//10**(length2-1) * 10**(length2-1)
            length2 -= 1
        return output
