class Solution:
    def reorganizeString(self, S: str) -> str:
        ans = ""
        c = Counter(S)
        pq = [(-value, key) for key, value in c.items()]
        heapq.heapify(pq)
        # => pq = []
        # => for key, value in c.items():
        # =>    heapq.heappusj(heap, [-value,key])
        p_a, p_b = 0, ''
        while pq:
            a,b = heapq.heappop(pq)
            ans += b
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(ans) != len(S):
            return ""
        else:
            return ans
