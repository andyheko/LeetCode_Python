class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = defaultdict(list)
        res = []
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            flightMap[origin].append(dest)
        # sort in lexical order
        for origin, itinerary in flightMap.items():
            itinerary.sort(reverse=True)
        # dfs
        def dfs(origin):
            while flightMap[origin]:
                nextDest = flightMap[origin].pop()
                dfs(nextDest)
            res.append(origin)

        dfs('JFK')
        return res[::-1] # caution!!!!


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flightMap = defaultdict(list)
        res = []
        stack = ['JFK']
        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            flightMap[origin].append(dest)
        # sort in lexical order
        for origin, itinerary in flightMap.items():
            itinerary.sort(reverse=True)

        while stack:
            while flightMap[stack[-1]]:
                next = flightMap[stack[-1]].pop()
                stack.append(next)
            res.append(stack.pop())

        return res[::-1] # caution!!!!
