class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s)+1)]
        # base case initialization
        dp[0] = 1

        for i in range(1, len(dp)):
            # for single-digit
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            # for two-digit
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]
        
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        pre = 1
        ppre = 0
        for i in range(1, len(s) + 1):
            temp = pre
            if s[i - 1] == "0":
                pre = 0
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                pre += ppre
            ppre = temp
        return pre
