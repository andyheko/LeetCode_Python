class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []
        dq = deque() # store index
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1: # if out of k range window
                dq.popleft() # pop the leftmost in dq
            while dq and nums[dq[-1]] < nums[i]: # pop number in dq smaller than curr
                dq.pop()
            dq.append(i)
            if i >= k - 1: # when i==k-1, full window begins
                res.append(nums[dq[0]])
        return res
