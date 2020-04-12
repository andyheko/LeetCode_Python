class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            maximum = max(stones)
            stones.remove(maximum)
            second = max(stones)
            stones.remove(second)

            if maximum != second:
                stones.append(maximum - second)
        if not stones:
            return 0
        return stones[0]
