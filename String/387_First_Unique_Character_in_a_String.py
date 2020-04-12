class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for idx, c in enumerate(s):
            if seen[c] == 1:
                return idx
        return -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)

        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1    
