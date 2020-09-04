class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def twoSumSmaller(nums, startIndex, target):
            count = 0
            left = startIndex
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    count += right - left # plus combinations between right, left
                    left += 1
                else:
                    right -= 1
            return count
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            count += twoSumSmaller(nums, i + 1, target - nums[i])
        return count


def maximumContainer(n, cost, m):
    count, curr, r = 0, 0, 0
    curr = n / c
    count += curr
    while curr > m:
        curr, r = (curr + r) / m, (curr + r) % r
        count += curr
    print(count)
