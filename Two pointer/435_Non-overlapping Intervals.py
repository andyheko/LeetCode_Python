class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, count = float('-inf'), 0
        for [left, right] in sorted(intervals, key=lambda x:x[1]):
            if left >= end: # not overlap, update end to the right of newest interval
                end = right
            else:
                count += 1 # overlap
        return count
