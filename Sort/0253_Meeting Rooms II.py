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

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        rooms = 0
        #seperate and sort start and end time
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        L = len(intervals)

        start_pointer = 0
        end_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                rooms -= 1
                end_pointer += 1

            rooms += 1
            start_pointer += 1
        return rooms
