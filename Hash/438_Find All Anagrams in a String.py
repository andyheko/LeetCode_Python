class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter()

        res = []
        for i in range(ns): # sliding window on string s
            s_count[s[i]] += 1 # add letter from right side of window into s_count
            if i >= np: # keep sliding window length == np
                if s_count[s[i-np]] == 1: # remove letter from left side of window
                    del s_count[s[i-np]]
                else:
                    s_count[s[i-np]] -= 1

            if p_count == s_count:
                res.append(i-np+1)

        return res
