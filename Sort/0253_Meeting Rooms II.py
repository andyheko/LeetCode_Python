class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = [] # heap initialization

        intervals.sort(key=lambda x: x[0]) # sort meeting by start time

        heapq.heappush(rooms, intervals[0][1]) # push first meeting end time

        for i in intervals[1:]:
            if rooms[0] <= i[0]: # if earlist room end time <= new meeting start time
                heapq.heappop(rooms) # pop the min room emd time
            heapq.heappush(rooms, i[1]) # push new room end time in order

        return len(rooms)
