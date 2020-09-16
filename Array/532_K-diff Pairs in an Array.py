class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 1
        ans = 0
        n = len(nums)
        while left < n and right < n:
            if left == right or nums[right] - nums[left] < k: # move right pointer
                right += 1
            elif nums[right] - nums[left] > k: # move left pointer
                left += 1
            else: # find the pair, move left pointer
                left += 1
                ans += 1
                while left < n and nums[left] == nums[left-1]: # if left pointer same # careful the order between and
                    left += 1
        return ans

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = Counter(nums)
        for c in counter:
            if k == 0 and counter[c] > 1: # if k==0, only one (c, c)
                ans += 1
            elif k > 0 and c + k in counter: # else, find, (c, c+k)
                ans += 1
        return ans
