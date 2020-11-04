'''
- divide and conquer

- if input is digit, return [input]
- if input in memo, return memo[input]
- iterate through, if '+-*',
- recursion on left and on right sides
- helper(res1, res2, input[i]), res.append()
- memo[intput] = res
- return res
- def helper(m, n, op)

'''

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def helper(m, n, op):
            if op == '+':
                return m+n
            elif op == '-':
                return m-n
            elif op == '*':
                return m*n

        res = []
        memo = {}
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input]
        for i in range(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(helper(j, k, input[i]))
        memo[input] = res
        return res
    
