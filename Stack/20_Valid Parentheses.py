class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for c in s:
            if c in dict:
                stack.append(dict[c])
            elif not stack or c != stack.pop():
                return False

        if not stack:
            return True
