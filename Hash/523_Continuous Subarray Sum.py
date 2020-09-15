class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sumTable = defaultdict(int) # {acc : i}
        sumTable[0] = -1 # impartant !!! acc == 0 at -1 position
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            if k != 0:
                acc %= k
            if acc in sumTable: # sums == n*k between sumTalbe[acc] and i
                if i - sumTable[acc] > 1: # make sure
                    return True
            else:
                sumTable[acc] = i
        return False
