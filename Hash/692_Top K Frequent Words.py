class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        ans = count.keys()
        ans = sorted(ans, key = lambda w: (-count[w], w)) # -count[w] means reversed sorting of count frequendy, w means when frequency is equal, compare in alphabetical order
        return ans[:k]
