class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        left = 0
        right = len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True

            # for reapeate charater case
            elif nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1

            elif nums[right] >= nums[mid]:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
        
