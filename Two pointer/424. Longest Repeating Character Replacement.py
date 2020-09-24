class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 # the length of the largest window so far
        maxf = 0 # the max frequency of any character seen so far
        count = collections.defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res < maxf + k: # maxf + k == max # of repeating letters so far
                res += 1
            else:
                count[s[i-res]] -= 1 # move the left most point
        return res
