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
