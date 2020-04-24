class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = total = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        for num in nums:
            total += num
            count += cache[total - k]
            cache[total] += 1
        return count
