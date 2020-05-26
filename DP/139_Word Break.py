class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s) # dp[i] is True if w ends at index of i in s & True before the begining of the w ( dp[i-len(w)] is True )

        for i in range(len(s)):#i: the index representing end of w in s
            for w in wordDict:
                if w == s[i-len(w)+1: i+1] and (dp[i-len(w)] or i-len(w) == -1):
                    dp[i] = True
                    break

        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True

        for i in range(1, len(s)+1):#i: (the index + 1) representing end of w in s
            for w in wordDict:
                if w == s[i-len(w): i] and dp[i-len(w)]:
                    dp[i] = True
                    break

        return dp[-1]
