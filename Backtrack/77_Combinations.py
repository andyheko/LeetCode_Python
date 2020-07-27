class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, curr):
            if len(curr) == k: # if combination is done
                output.append(curr[:])

            for i in range(first, n+1):
                curr.append(i) # add i into current combination
                backtrack(i + 1, curr) # use next integer to complete combination
                curr.pop() # backtrack

        output = []
        backtrack(1, [])
        return output
