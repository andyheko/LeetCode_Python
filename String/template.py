class Trie:
    def __init__(self, val):
        self.char = val
        self.wc = 0 # word count
        self.children = {}

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Trie('#')
        for s in strs:
            cur = root
            for c in s:
                if c not in cur.children: # if not in children
                    cur.children[c] = Trie(c) # create in childre
                cur = cur.children[c] # move cur to child
                cur.wc += 1 # word count ++
        res = ''
        cur = root
        pre = None
        while pre != cur:
            pre = cur
            for child in cur.children.values():
                if child.wc == len(strs): # if wc == len of string, is common prefix
                    res += child.char
                    cur = child # move cur to child
        return res
