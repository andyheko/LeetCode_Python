class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        repeat = []
        def helper(n, repeat):
            if n == 1:
                return True
            else:
                sum = 0
                for i in str(n):
                    sum += int(i) ** 2
                if sum in repeat:
                    return False
                else:
                    repeat.append(sum)
                    return helper(sum, repeat)
        return helper(n, repeat)
