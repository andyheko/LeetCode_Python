class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(last_pos, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i # update the last position
        return last_pos == 0 # return True if last position at 0 else False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = 0
        for i in range(len(nums)):
            if last_pos >= i and i + nums[i] >= last_pos:
                last_pos = i + nums[i] # update the last position

        return last_pos >= len(nums) - 1 # return True if last position at len(nums)-1 else False
