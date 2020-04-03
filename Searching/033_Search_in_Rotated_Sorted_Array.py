# Iteration Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[right] >= nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

# Recursive Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRecursive(nums, left, right, target):
            if left > right:
                return -1
            else:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                if nums[right] >= nums[mid]:
                    if nums[mid] < target <= nums[right]:
                        return searchRecursive(nums, mid+1, right, target)
                    else:
                        return searchRecursive(nums, left, mid-1, target)
                else:
                    if nums[left] <= target < nums[mid]:
                        return searchRecursive(nums, left, mid-1, target)
                    else:
                        return searchRecursive(nums, mid+1, right, target)
        return searchRecursive(nums, 0, len(nums)-1, target)
        
# Recursive Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchRecursive(nums, 0, len(nums)-1, target)
    def searchRecursive(self, nums, left, right, target):
        if left > right:
            return -1
        else:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[right] >= nums[mid]:
                if nums[mid] < target <= nums[right]:
                    return self.searchRecursive(nums, mid+1, right, target)
                else:
                    return self.searchRecursive(nums, left, mid-1, target)
            else:
                if nums[left] <= target < nums[mid]:
                    return self.searchRecursive(nums, left, mid-1, target)
                else:
                    return self.searchRecursive(nums, mid+1, right, target)
