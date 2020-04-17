class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L = [0] * length #product of all elements to the left of element at index i
        R = [0] * length #product of all elements to the right of element at index i
        output = [0] * length


        L[0] = 1 # L for first element
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        R[length-1] = 1 # R for last element
        #for i in range(length-2, -1, -1): # from length-2 to 0
        for i in reversed(range(length-1)): # from length-2 to 0
            R[i] = R[i+1] * nums[i+1]

        for i in range(length):
            output[i] = L[i] * R[i]

        return output

### Solution 2 : O(1) Space Complexity

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        output = [0] * length


        output[0] = 1 # output present product of elements to the left of index i
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]

        R = 1 # R as variable to contain product of elements to the right of index i
        for i in reversed(range(length)): # from length-1 to 0
            output[i] = output[i] * R
            R *= nums[i] # update R

        return output
