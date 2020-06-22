class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2): # the last two has been tried
			if nums[i] > 0: break # since in sorted order, no need to consider all positive number
			if i > 0 and nums[i] == nums[i-1]: continue # has used it as target before, skip this loop

			l, r = i + 1, length - 1
			while l < r:
				total = nums[i] + nums[l] + nums[r]

				if total < 0: #need bigeer
					l += 1
				elif total > 0: #need smaller
					r -= 1
				else: #jackpot
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l+1]: # move l and r to next different number, avoid duplicate number
						l += 1
					while l<r and nums[r]==nums[r-1]: # move l and r to next different number, avoid duplicate number
						r -= 1
					l += 1
					r -= 1
		return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dup = set()
        for i in range(len(nums)):
            dict = {}
            target = 0 - nums[i]
            for j in range(i+1, len(nums)):
                if target - nums[j] not in dict:
                    dict[nums[j]] = j
                else:
                    min_val = min(nums[i], nums[j], target - nums[j])
                    max_val = max(nums[i], nums[j], target - nums[j])
                    if (min_val, max_val) not in dup:
                        dup.add((min_val, max_val))
                        ans.append([nums[i], nums[j], target - nums[j]])
        return ans
