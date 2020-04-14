class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        total = 0
        for i in range(len(shift)):
            if shift[i][0] == 0:
                total -= shift[i][1]
            elif shift[i][0] == 1:
                total += shift[i][1]
        while total < 0:
            a = s[0]
            s = s[1:]
            s = s + a
            total+=1
        while total > 0:
            a = s[-1]
            s = s[:-1]
            s = a + s
            total -= 1
        return s
