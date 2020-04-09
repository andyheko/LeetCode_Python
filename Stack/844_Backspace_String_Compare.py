class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(a):
            ans = []
            for c in a:
                if c == '#' and ans:
                    ans.pop()
                elif c != '#':
                    ans.append(c)
            return ans
        return build(S) == build(T)
