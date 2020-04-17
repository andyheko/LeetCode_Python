class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for c in ransomNote:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for m in magazine:
            if m in count:
                count[m] -= 1

        for i in count:
            if count[i] > 0:
                return False

        return True
