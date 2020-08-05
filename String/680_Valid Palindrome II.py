class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                sl, sr = s[:l] + s[l+1:], s[:r] + s[r+1:]
                return sl == sl[::-1] or sr == sr[::-1]
            l += 1
            r -= 1

        return True
