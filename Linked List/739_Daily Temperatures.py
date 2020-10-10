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

    # [73, 74, 75, 71, 69, 72, 76, 73]
    # stack = [0] ans = [0,0,0,0,0,0,0,0]
    # stack = [1] ans = [1,0,0,0,0,0,0,0]
    # stack = [2] ans = [1,1,0,0,0,0,0,0]
    # stack = [2, 3] ans = [1,1,0,0,0,0,0,0]
    # stack = [2, 3] ans = [1,1,0,0,0,0,0,0]
    # stack = [2, 3, 4] ans = [1,1,0,0,0,0,0,0]
    # stack = [2, 5] ans = [1,1,0,2,1,0,0,0]
    # stack = [2, 5] ans = [1,1,0,2,1,0,0,0]
    # stack = [6] ans = [1,1,4,2,1,1,0,0]
    # stack = [7] ans = [1,1,4,2,1,1,0,0]
