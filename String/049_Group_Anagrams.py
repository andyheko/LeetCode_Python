class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for word in strs:
                output[tuple(sorted(word))].append(word)
        return output.values()
