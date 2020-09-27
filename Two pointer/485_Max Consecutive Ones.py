class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                maxL = max(maxL, r - l + 1)
            else:
                l = r + 1
        return maxL
