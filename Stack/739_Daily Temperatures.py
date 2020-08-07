class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = [] # store index from hot to cold
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t: # while cur T > last T in stack
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)

        return ans
