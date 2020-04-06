class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        inflow = [0] * (N+1)
        outflow = [0] * (N+1)
        for a, b in trust:
            outflow[a] = -1
            intflow[b] += 1
        for i in range(1, N+1):
            if inflow[i] == (N-1) and outflow[i] != -1:
                return i
        return -1
