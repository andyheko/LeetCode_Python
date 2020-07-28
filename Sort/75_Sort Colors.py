class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, curr, r = 0, 0, len(nums) -1

        while curr <= r:
            if nums[curr] == 0: # if red
                nums[l], nums[curr] = nums[curr], nums[l]
                l += 1
                curr += 1
            elif nums[curr] == 1: # if white
                curr += 1
            else: # if red
                nums[curr], nums[r] = nums[r], nums[curr]
                r -= 1
