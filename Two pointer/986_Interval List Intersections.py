class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0 # index of interval in A, B
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0]) # startpoint of intersection
            end = min(A[i][1], B[j][1]) # endpoint of intersection
            if start <= end:
                ans.append([start, end])

            # move the smallest endpoint interval forward
            if A[i][1] < B[j][1]:
                i += 1 # move A forward
            else:
                j += 1 # move B forward

        return ans
