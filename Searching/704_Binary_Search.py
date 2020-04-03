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

### Recursive Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, left, right, target):
            if left > right:
                return -1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    return helper(nums, mid+1, right, target)
                else:
                    return helper(nums, left, mid-1, target)

        return helper(nums, 0, len(nums)-1, target)

### Recursive Solution 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)
    def helper(self, nums, left, right, target):
        if left > right:
            return -1
        else:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return self.helper(nums, mid+1, right, target)
            else:
                return self.helper(nums, left, mid-1, target)
