class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        n = len(intervals)
        output = []
        while idx < n and newInterval[0] > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1

        #add new interval
        if not output or output[-1][1] < newInterval[0]: # if no overlap
            output.append(newInterval)
        else: # if overlap
            output[-1][1] = max(output[-1][1], newInterval[1])

        while idx < n:
            if output[-1][1] < intervals[idx][0]: # if no overlap
                output.append(intervals[idx])
            else: # if overlap
                output[-1][1] = max(output[-1][1], intervals[idx][1])
            idx += 1
        return output

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        res = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if res and res[-1][1] >= i[0]: # overlap
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
