class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end, count = float('-inf'), 0
        points.sort(key=lambda x : x[1]) # sort by right of points
        for left, right in points:
            if left > end: # not overlap, count += 1, update end to the right of point
                count += 1
                end = right
        return count
