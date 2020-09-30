class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(node): # find friend
            if uf[node] != -1: # has direct friend
                return find(uf[node])
            return node # no direct friend, return node

        n = len(M)
        uf = {x: -1 for x in range(n)} # initial every x: -1
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1 and find(i) != find(j): # direct friend and not friend yet
                    uf[find(i)] = find(j) # mark as friend
        return sum([1 for k, v in uf.items() if v == -1]) # count # with v==-1 quals # of groups
