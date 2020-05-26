class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def paint_cost(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            total_cost = costs[n][color]
            if n == len(costs) - 1:
                pass
            elif color == 0: # red
                total_cost += min(paint_cost(n+1, 1), paint_cost(n+1, 2))
            elif color == 1: # green
                total_cost += min(paint_cost(n+1, 0), paint_cost(n+1, 2))
            else: # blue
                total_cost += min(paint_cost(n+1, 0), paint_cost(n+1, 1))
            self.memo[(n, color)] = total_cost
            return total_cost

        if costs == []:
            return 0
        self.memo = {}
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
# Time:O(n)
# Space: O(n)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        for n in reversed(range(len(costs)-1)): # n from len(costs)-2 to 0
            costs[n][0] += min(costs[n+1][1], costs[n+1][2]) # cost of painting nth house red
            costs[n][1] += min(costs[n+1][0], costs[n+1][2]) # cost of painting nth house green
            costs[n][2] += min(costs[n+1][0], costs[n+1][1]) # cost of painting nth house blue

        return min(costs[0])

# Time:O(n)
# Space: O(1)

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0

        for n in range(1, len(costs)): # n from 1 to len(costs)
            costs[n][0] += min(costs[n-1][1], costs[n-1][2]) # cost of painting nth house red
            costs[n][1] += min(costs[n-1][0], costs[n-1][2]) # cost of painting nth house green
            costs[n][2] += min(costs[n-1][0], costs[n-1][1]) # cost of painting nth house blue

        return min(costs[-1])
# Time:O(n)
# Space: O(1)
