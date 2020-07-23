class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            for i in range(len(output)):
                output.append(output[i] + [num])
        return output

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(tmp, start, end):
            ans.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(tmp, i+1, end)
                tmp.pop()
        ans = []
        backtrack([], 0, len(nums))
        return ans
