class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        frequency = sorted(counter.items(), key=lambda x:x[1]) # sort dictionary
        fmax = frequency.pop() # pop the character with max frequency
        idle = (fmax[1] - 1) * n # initial idle time
        while frequency and idle > 0:
            fnext = frequency.pop()[1] # next max frequency
            idle -= min(fmax[1]-1, fnext) # min: in case fnext == fmax[1]
        idle = max(0, idle) # in case idle becomes < 0
        return idle + len(tasks)
