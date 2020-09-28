class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = 0
        r = n - k
        totalSum = sum(cardPoints[r:]) # initial totalSum = rightSum
        ans = totalSum
        for i in range(k):# sliding window, left section++, right section--
            totalSum += cardPoints[l] - cardPoints[r]
            ans = max(ans, totalSum)
            l += 1 # left pointer move right
            r += 1 # right pointer move right

        return ans

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = k - 1
        r = n - 1
        totalSum = sum(cardPoints[:k]) # initial totalSum = leftSum
        ans = totalSum
        for i in range(k):# sliding window, left section--, right section++
            totalSum += cardPoints[r] - cardPoints[l]
            ans = max(ans, totalSum)
            l -= 1 # left pointer move left
            r -= 1 # right pointer move left

        return ans
