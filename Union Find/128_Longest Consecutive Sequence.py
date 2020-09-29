class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]: # important when duplicate elements
                if nums[i] == nums[i-1] + 1:
                    curr_streak += 1
                else:
                    longest_streak = max(longest_streak, curr_streak)
                    curr_streak = 1

        return max(longest_streak, curr_streak) # important when all elements are consecutive !!!


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_streak = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set: ### important not to re-search smaller cosecutive nums
                curr = num
                curr_streak = 1

                while curr + 1 in num_set:
                    curr += 1
                    curr_streak += 1

                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
