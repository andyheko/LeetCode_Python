class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def search(sub, target):
            start, end = 0, len(sub) - 1
            while end >= start:
                mid = (start + end) // 2
                if sub[mid] > target:
                    end = mid - 1
                elif sub[mid] < target:
                    start = mid + 1
                else:
                    return mid
            return start

        sub = []
        for num in nums:
            pos = search(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        return len(sub)
