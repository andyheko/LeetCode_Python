class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1

        # find longest non-increasing suffix from rightmost
        while right >= 1 and nums[right-1] >= nums[right]:
            right -= 1
        if right == 0: # while nums is descending
            return nums.reverse()

        # find pivot
        pivot = right - 1
        # find rightmost succesor which > pivot
        for i in range(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                successor = i
                break
        # swap pivot and successor
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        # reverse suffix
        l, r = pivot+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
