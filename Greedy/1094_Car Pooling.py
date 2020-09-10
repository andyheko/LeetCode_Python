class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L = []
        for n, i, j in trips:
            L.append([i, n])
            L.append([j, -n])
        L.sort(key=lambda x:(x[0], x[1])) # important sort x[0] then sort x[1]
                                        # corner case i ==j, -n first, then n
        for i, v in L:
            capacity -= v
            if capacity < 0:
                return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for n, i, j in trips:
            heapq.heappush(heap, (i, n))
            heapq.heappush(heap, (j, -n))

        while heap:
            capacity -= heapq.heappop(heap)[1]
            if capacity < 0:
                return False
        return True
