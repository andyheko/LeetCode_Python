class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()

        ans = []
        candidates.sort(reverse=True)
        backtrack([], 0, len(candidates), target)
        return ans
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(target, index, path):
            if target < 0:
                return  # backtracking
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target-candidates[i], i, path+[candidates[i]])

        dfs(target, 0, [])
        return res
