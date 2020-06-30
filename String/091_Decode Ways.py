class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s)+1)]
        # base case initialization
        dp[0:2] = [1, 1]

        for i in range(2, len(dp)):
            # for single-digit
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # for two-digit
            two_digit = int(s[i-2 :i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]
