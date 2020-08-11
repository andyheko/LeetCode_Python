class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]] # store all possible sequences we got to the element

        while layer:
            newlayer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word] # return all found sequences
                else:
                    for i in range(len(word)): # change every possible letter and check if it's in wordset
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            newWord = word[:i] + c + word[i+1:]
                            if newWord in wordSet:
                                newlayer[newWord] += [j + [newWord] for j in layer[word]] # add newWord to all sequences
            wordSet -= set(newlayer.keys()) # remove from dictionary
            layer = newlayer # move to new layer

        return []
