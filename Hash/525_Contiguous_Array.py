class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dict={count:index}
        dict = {0:-1} #inital count 0 at index -1
        count = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            if nums[i] == 1:
                count += 1
            if count in dict:
                max_length = max(max_length, i - dict[count])
            else:
                dict[count] = i
        return max_length
