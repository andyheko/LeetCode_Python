class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c] # move down the node
        node['$'] = True # mark as leaf

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_node(word, node):
            for i, c in enumerate(word):
                if not c in node:
                    if c == '.': # if current c is '.'
                        for x in node: # check all possible nodes at this level
                            if x != '$' and search_node(word[i+1:], node[x]):
                                return True
                    # if current c is not '.' or no node leads to answer
                    return False
                # if found c in node, go down the node
                else:
                    node = node[c]
            return '$' in node # check if current node is a leaf

        return search_node(word, self.trie)
