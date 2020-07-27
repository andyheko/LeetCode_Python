class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = defaultdict(int)
        for item in s:
            dic[item] = dic[item] + 1
        count = 0
        for val in dic.values():
            if val % 2 == 1:
                count += 1
            if count > 1: # odd string => count == 1
                return False
        return True
