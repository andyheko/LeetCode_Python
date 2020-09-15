class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # for odd case, like "aba"
            odd = self.helper(s, i, i)
            if len(odd) > len(res):
                res = odd
            # for even case, like "abba"
            even = self.helper(s, i, i+1)
            if len(even) > len(res):
                res = even
        return res


    # starting at l,r expand outwards to find the biggest palindrome
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r] # *important*


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # for odd case, like "aba"
            odd = self.helper(s, i, i)
            # for even case, like "abba"
            even = self.helper(s, i, i+1)

            res = max(res, odd, even, key=len)
        return res

    # starting at l,r expand outwards to find the biggest palindrome
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r] # *important*
