class Solution:
    def findKthLargest(self, nums, k):
        # [3, 2, 1, 5, 6, 4], 2th larget
        # choose the right-most element as pivot
        def partition(nums, l, r):
            low = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[low] = nums[low], nums[i]
                    low += 1 # increase the index of smaller element
            nums[low], nums[r] = nums[r], nums[low]
            return low # pivot index

        pos = partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else: # pos == len(nums) - k, the index of kth largest element
            return nums[pos]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
class Solution:
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
