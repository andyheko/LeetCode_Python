class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i < 2:
                        dp[i] = 0 + 2
                    else:
                        dp[i] = dp[i-2] + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                maxLen = max(maxLen, dp[i])
        return maxLen

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        stack = []
        stack.append(-1) # reference idx
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else: # encounter ')'
                stack.pop()
                if not stack: # if stack is empty, add reference idx
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1]) # update len
        return maxLen

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        maxLen = 0
        for i in range(len(s)): # scan from left to right
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2 * right)
            elif right > left: # reset pointers
                left = right = 0

        right = left = 0
        for i in range(len(s)-1, -1, -1): # scan from right to left
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                maxLen = max(maxLen, 2 * right)
            elif left > right: # reset pointers
                left = right = 0

        return maxLen
