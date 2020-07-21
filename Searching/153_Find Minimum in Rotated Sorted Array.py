class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        # if no inflection point
        if nums[end] > nums[0]:
            return nums[0]

        while end >= start:
            mid = (start + end) // 2
            # find the infleciton point
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
