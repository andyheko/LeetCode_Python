class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # sliding window
        # left, right: index of two pointer
        start = 0
        max_L = 0
        n = len(s)
        seen = {}
        if n < 3:
            return n

        for i, c in enumerate(s):
            if len(seen) >= 2 and c not in seen:
                del_idx = min(seen.values())
                start = seen[s[del_idx]] + 1
                del seen[s[del_idx]]
            seen[c] = i
            max_L = max(max_L, i - start + 1)
        return max_L
