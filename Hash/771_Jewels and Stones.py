class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        dict = {}
        for j in J:
            dict[j] = 0
        for s in S:
            if s in dict:
                count += 1
        return count

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        dict = set(J)
        for s in S:
            if s in dict:
                count += 1
        return count
