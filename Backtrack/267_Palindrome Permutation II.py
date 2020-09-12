class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = []
        counter = Counter(s)
        odd = []
        for k, v in counter.items():
            if v % 2 != 0: # if odd amount number ex a, bbb
                odd.append(k)

        def backtrack(tmp):
            if len(tmp) == len(s):
                ans.append(tmp)
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    backtrack(k+tmp+k)
                    counter[k] += 2

        if len(odd) > 1: # more than 1 odd amount nubmer, can't be palindrome
            return []
        elif len(odd) == 1: # only 1 odd amount number
            counter[odd[0]] -= 1
            backtrack(odd[0])
        else: # no odd amount number
            backtrack('')
        return ans
