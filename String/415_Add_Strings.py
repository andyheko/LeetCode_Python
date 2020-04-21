class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)

        s = 0
        decimal = 0
        for i in range(l1-1, -1, -1):
            s += int(num1[i]) * (10 ** decimal)
            decimal += 1
        decimal = 0
        for j in range(l2-1, -1, -1):
            s += int(num2[j]) * (10 ** decimal)
            decimal += 1

        return str(s)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)

        s1 = 0
        s2 = 0
        for i in range(l1):
            s1 = s1 * 10 + int(num1[i])
        for j in range(l2):
            s2 = s2 * 10 + int(num2[j])

        return str(s1 + s2)
