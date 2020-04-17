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
