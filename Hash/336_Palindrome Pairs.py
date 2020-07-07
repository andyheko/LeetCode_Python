class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # for case #3, word 1, find prefix, CAT
        def all_valid_prefixes(word): # find a prefix if the suffix forms a palindrome
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes
        # for case #2, word 2, find suffix, TAC
        def all_valid_suffixes(word): # find a suffix if the prefix forms a palindrome
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i+1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        ans = []
        for i, word in enumerate(words):
            reversed_word = word[::-1]
            # ans for case #1
            if reversed_word in word_lookup and i != word_lookup[reversed_word]:
                ans.append([i, word_lookup[reversed_word]])

            # ans for case #2
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    ans.append([word_lookup[reversed_suffix], i])

            # ans for case #3
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    ans.append([i, word_lookup[reversed_prefix]])

        return ans
