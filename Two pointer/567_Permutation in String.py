class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()

        n1 = len(s1)
        n2 = len(s2)
        for i in range(n2):
            s2_count[s2[i]] += 1
            if i >= n1:
                if s2_count[s2[i-n1]] == 1:
                    del s2_count[s2[i-n1]]
                else:
                    s2_count[s2[i-n1]] -= 1
            if s1_count == s2_count:
                return True
        return False
