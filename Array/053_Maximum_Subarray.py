'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

#### Divide and Conquer Solution O(nlogn)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left > right:
            return 0
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        x_left = self.helper(nums, left, mid)
        x_right = self.helper(nums, mid+1, right)
        left_max, right_max = 0, 0
        left_sum, right_sum = 0, 0
        # for left half
        for i in range(mid-1, left-1, -1):
            left_sum += nums[i]
            left_max = max(left_sum, left_max)
        # for right half
        for i in range(mid+1, right+1, 1):
            right_sum += nums[i]
            right_max = max(right_sum, right_max)
        return max(x_left, x_right, max(0, left_max) + max(0, right_max) + nums[mid])
