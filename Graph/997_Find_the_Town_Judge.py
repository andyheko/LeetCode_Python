class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inflow = [0] * (N+1)
        outflow = [0] * (N+1)
        for a, b in trust:
            inflow[a] = -1
            outflow[b] += 1
        for i in range(1, N+1):
            if outflow[i] == (N-1) and inflow[i] != -1:
                return i
        return -1
