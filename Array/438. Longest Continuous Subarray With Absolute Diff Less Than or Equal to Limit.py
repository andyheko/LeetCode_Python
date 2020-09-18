class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen = 0
        i = 0
        minQ = deque()
        maxQ = deque()
        for j in range(len(nums)):
            while maxQ and maxQ[-1] < nums[j]: maxQ.pop()
            while minQ and minQ[-1] > nums[j]: minQ.pop()

            maxQ.append(nums[j])
            minQ.append(nums[j])
            if maxQ[0] - minQ[0] <= limit:
                maxLen = max(maxLen, j - i + 1)

            else:
                if maxQ[0] == nums[i]:
                    maxQ.popleft()
                if minQ[0] == nums[i]:
                    minQ.popleft()
                i += 1
        return maxLen
