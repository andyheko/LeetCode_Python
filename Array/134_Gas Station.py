class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        curr_tank = 0
        start_station = 0
        for station in range(len(gas)):
            total_tank += gas[station] - cost[station]
            curr_tank += gas[station] - cost[station]
            if curr_tank < 0: # could not get to next station
                start_station = station + 1
                curr_tank = 0

        return -1 if total_tank < 0 else start_station
