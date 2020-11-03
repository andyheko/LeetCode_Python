class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def isCyclic(currCourse):
            if seen[currCourse]: # detect cycle
                return True
            # before backtrack
            seen[currCourse] = True
            # backtracking
            ret = False
            for child in courseDict[currCourse]:
                ret = isCyclic(child) # mark every child as seen
                if ret: # if any cycle, res == True
                    break
            # after backtracking
            seen[currCourse] = False
            return ret

        courseDict = defaultdict(list) # graph's adj. list
        for relation in prerequisites: # build add. list
            nextCourse, prevCourse = relation[0], relation[1]
            courseDict[prevCourse].append(nextCourse) # directed graph

        seen = [False] * numCourses # mark seen as True
        for currCourse in range(numCourses):
            if isCyclic(currCourse):
                return False
        return True # finish loop, call not seen => DAG => true
