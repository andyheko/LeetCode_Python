class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftbalance = rightbalance = 0
        for i in range(len(s)):
            if s[i] in '(*':
                leftbalance += 1
            else:
                leftbalance -= 1

            if s[len(s) - 1 - i] in '*)':
                rightbalance += 1
            else:
                rightbalance -= 1

            # if any balance go negative, the order of paranthesis is wrong
            if leftbalance < 0 or rightbalance < 0:
                return False
        return True
