class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.findall(r"\w+", paragraph.lower())
        count = collections.Counter(x for x in paragraph if x not in banned)
        return count.most_common(1)[0][0]

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        count = Counter(word for word in words if word not in banned)

        res, num = '', 0
        for word, n in count.items():
            if n > num:
                num = n
                res = word
        return res
