class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # create data structure
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # populate adj_list and in_degree
        for word1, word2 in zip(words, words[1:]):
            # check if word1 and word2 are valid
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            # contruct graph
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    if ch2 not in adj_list[ch1]:
                        adj_list[ch1].add(ch2)
                        in_degree[ch2] += 1
                    break

        #topological sort
        res = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            node = queue.popleft()
            res.append(node)
            for ch in adj_list[node]:
                in_degree[ch] -= 1
                if in_degree[ch] == 0:
                    queue.append(ch)

        if len(res) < len(in_degree):
            return ""
        return "".join(res)
