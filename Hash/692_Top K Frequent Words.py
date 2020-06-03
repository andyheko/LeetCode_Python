class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        ans = count.keys()
        ans = sorted(ans, key = lambda w: (-count[w], w))
        return ans[:k]
