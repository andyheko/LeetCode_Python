class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        lowest = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]

            if profit < prices[i] - lowest:
                profit = prices[i] - lowest

        return profit
