class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        dict = {}
        n = len(s)
        left, right = 0 , 0
        maxLength = 0
        while left < n and right < n:
            if s[right] not in dict:
                dict[s[right]] = 1
                right += 1
                maxLength = max(maxLength, right - left)
            else:
                del dict[s[left]]
                left += 1
        return maxLength

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        dict = {}
        n = len(s)
        maxLength, start = 0, 0

        for i, c in enumerate(s):
            if c in dict and start <= dict[c]:
                start = dict[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            dict[c] = i

        return maxLength
