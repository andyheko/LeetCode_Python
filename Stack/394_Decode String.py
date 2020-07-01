class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = ''
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c) # ex 101
            elif c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num * curString # * remembet to add prevString when dealing with ]] ex. [a2[cc]]

            else:
                curString += c
        return curString
