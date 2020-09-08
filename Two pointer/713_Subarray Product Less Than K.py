class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, prod, count = 0, 1, 0
        for end in range(len(nums)):
            prod *= nums[end]

            while prod >= k and start <= end:
                prod /= nums[start]
                start += 1

            count += end - start + 1

        return count
