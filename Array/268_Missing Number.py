class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        expectedSum = 0
        for i in range(len(nums)):
            sum += nums[i]
            expectedSum += i+1
        return expectedSum - sum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        for num in range(len(nums) + 1):
            if num not in numSet:
                return num
