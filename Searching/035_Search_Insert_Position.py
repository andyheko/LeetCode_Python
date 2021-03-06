class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target < nums[0]:
            return 0
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                if left > len(nums):
                    return len(nums)
                else:
                    if nums[left] > target:
                        return left
            else:
                right = mid - 1
                if right < 0:
                    return 0
                else:
                    if nums[right] < target:
                        return right + 1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        start = 0
        end = len(nums) - 1
        while end >= start:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target >= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start
