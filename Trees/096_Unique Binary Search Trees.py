class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1) # the number of unique BST for a sequence of length n
        G[0] = 1 # n = 0, n = 1

        for i in range(1, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
