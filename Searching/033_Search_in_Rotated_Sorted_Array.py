


# Recursive Solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRecursive(nums, left, right, target):
        	if left > right:
        		return -1

        	mid = (left + right) // 2
        	if nums[mid] == target:
        		return mid

        	if nums[left] <= nums[mid]:
        		if nums[left] <= target < nums[mid]:
        			return searchRecursive(nums, left, mid-1, target)
        		else:
        			return searchRecursive(nums, mid+1, right, target)
        	else:
        		if nums[mid] < target <= nums[right]:
        			return searchRecursive(nums, mid+1, right, target)
        		else:
        			return searchRecursive(nums, left, mid-1, target)

        return searchRecursive(nums, 0, len(nums)-1, target)
