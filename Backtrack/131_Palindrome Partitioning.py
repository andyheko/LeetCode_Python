class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(tmp, start, end):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(tmp, i+1, end)
                    tmp.pop()
        ans = []
        backtrack([], 0, len(s))
        return ans
