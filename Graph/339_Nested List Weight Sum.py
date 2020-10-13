# recursive DFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(list, depth):
            sum = 0
            for n in list:
                if n.isInteger():
                    sum += n.getInteger() * depth
                else:
                    sum += dfs(n.getList(), depth+1)
            return sum
        return dfs(nestedList, 1)

# iterative DFS
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n, 1)) # (node, depth)
        while stack:
            next, d = stack.pop()
            if next.isInteger():
                sum += d * next.getInteger()
            else:
                for i in next.getList():
                    stack.append((i, d+1))
        return sum
