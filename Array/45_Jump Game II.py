class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        jumps = 0
        currEnd = 0
        currFarthest = 0
        for i in range(len(nums) - 1):# from 0 to len(nums) - 2
            currFarthest = max(currFarthest, i + nums[i])
            if i == currEnd: # force to jump
                jumps += 1
                currEnd = currFarthest # update currEnd
                if currEnd >= len(nums) - 1: # check if alreay reach the end
                    break
        return jumps
