class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(tmp, i+1, end, target - candidates[i])
                    tmp.pop()

        ans = []
        candidates.sort(reverse=True)
        backtrack([], 0, len(candidates), target)
        return ans
