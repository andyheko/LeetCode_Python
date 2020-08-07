class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            max_temp = max(curr, curr * max_so_far, curr * min_so_far) ### avoid new max_so_far affects min_so_far
            min_so_far = min(curr, curr * max_so_far, curr * min_so_far)

            max_so_far = max_temp ### important part
            res = max(res, max_so_far)

        return res
