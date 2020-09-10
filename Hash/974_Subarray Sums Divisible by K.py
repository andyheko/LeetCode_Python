class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        mod_array = [0] * K # idx 0 ~ K-1: mod, val: count of mod
        mod_array[0] = 1
        res ,acc = 0, 0
        for a in A:
            acc += a
            res += mod_array[acc % K] # res adds count of the same mod
            mod_array[acc % K] += 1 # adds count of mod
        return res
