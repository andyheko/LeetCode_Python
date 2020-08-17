class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for student, score in items:
            d[student].append(score)
        for i in d:
            d[i] = sorted(d[i])[-5:]
        return [[i, sum(d[i]) // 5] for i in d]
