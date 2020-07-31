class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else: # sign = "/"
                    temp = stack.pop()
                    res = abs(temp) // num # careful ex. -3 // 2 = -2
                    if temp >= 0:
                        stack.append(res)
                    else:
                        stack.append(-res)
                # reset num and set sign
                num = 0
                sign = s[i]
        return sum(stack)   
