class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= s:
                ans = min(ans, i - left + 1)
                sum -= nums[left]
                left += 1


        return ans if ans != float('inf') else 0
