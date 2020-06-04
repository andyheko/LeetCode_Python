class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        ans = count.keys()
        ans = sorted(ans, key = lambda w: (-count[w], w)) # -count[w] means reversed sorting of count frequendy, w means when frequency is equal, compare in alphabetical order
        return ans[:k]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap) # turn a list into a heap in linear time
        return [heapq.heappop(heap)[1] for _ in range(k)]
