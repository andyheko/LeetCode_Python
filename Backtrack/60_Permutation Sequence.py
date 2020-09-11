class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1] # factorials lookup table
        nums = ['1'] # list of numbers
        for i in range(1, n):
            factorials.append(factorials[i-1] * i) # [0!,1!,2!, ... (n-1)!]
            nums.append(str(i+1)) # ['1', '2', ... 'n']
        k -= 1 # 0 ~ n!-1
        output = []
        for i in range(n-1, -1, -1):
            idx = k // factorials[i] # find the idx of nums for output
            k -= idx * factorials[i] # residual k

            output.append(nums[idx])
            del nums[idx]
        return ''.join(output)
