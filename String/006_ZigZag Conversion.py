class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):# *must caution*
            return s

        ans = [''] * numRows
        index, step = 0, 1

        for x in s:
            ans[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(ans)
