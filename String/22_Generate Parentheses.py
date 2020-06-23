class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                generate(S+'(', left+1, right)
            if right < left:
                generate(S+')', left, right+1)

        generate()
        return ans

        class Solution:
            def generateParenthesis(self, n: int) -> List[str]:
                if n == 0:
                    return ['']
                ans = []
                for c in range(n):
                    for left in self.generateParenthesis(c):
                        for right in self.generateParenthesis(n-c-1):
                            ans.append('({}){}'.format(left, right))
                return ans
