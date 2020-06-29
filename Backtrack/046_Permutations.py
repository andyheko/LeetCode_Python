class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start = 0):
            if start == n: # current permutation is done
                ans.append(nums[:])
            for i in range(start, n):
                # swap
                nums[start], nums[i] = nums[i], nums[start]
                # create all permutations
                backtrack(start+1)
                # backtrack, swap back
                nums[start], nums[i] = nums[i], nums[start]

        n = len(nums)
        ans = []
        backtrack()
        return ans
