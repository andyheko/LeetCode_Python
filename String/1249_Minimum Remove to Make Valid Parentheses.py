class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        status_dict = {} # store the validity of idx for '(' or ')'
        stack = [] # to store idx of '('
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                status_dict[i] = True # valid for ')'
                status_dict[stack[-1]] = True # valid for '('
                stack.pop()

        res = []
        for i, c in enumerate(s):
            if c == "(" or c == ")":
                if i in status_dict: # only append valid parenthesis
                    res.append(c)
            else:
                res.append(c)

        return "".join(res)
