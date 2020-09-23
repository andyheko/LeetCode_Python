class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number = 0
        if len(s) <= 1:
            return table[s[0]]
        i = 0
        while i < len(s):
            if i < len(s) - 1 and table[s[i+1]] > table[s[i]]: # ex.IV or IX
                number += table[s[i+1]] - table[s[i]]
                i += 1 # important!!!
            else: # last character or ex. III or LVIII
                number += table[s[i]]
            i += 1
        return number
