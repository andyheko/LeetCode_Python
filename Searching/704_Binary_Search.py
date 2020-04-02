class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        if len(nums) == 0:
            return -1
        while last >= first:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                first = mid + 1
            else:
                last = mid - 1
        return -1
