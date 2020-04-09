class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(a):
            ans = []
            for c in a:
                if c == '#' and ans:
                    ans.pop()
                elif c != '#':
                    ans.append(c)
            return ans
        return build(S) == build(T)

# Solution 2: Two pointer
class Solution(object):
    def backspaceCompare(self, S, T):
        def builder(a):
            skip = 0 # indicate how many character need to be skipped
            for c in reversed(a):
                if c == '#':
                    skip += 1
                # if encounter '#' previously, skip one character and reset skip
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(builder(S), builder(T)))
