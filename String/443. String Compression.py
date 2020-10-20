class Solution:
    def compress(self, chars: List[str]) -> int:
        left, i = 0, 0 # left is new chars idx
        while i < len(chars):
            curr = chars[i]
            count = 0
            while i < len(chars) and curr == chars[i]: # start count
                count += 1
                i += 1
            chars[left] = curr
            left += 1 # left is new chars idx
            if count > 1:
                for c in str(count): # count could > 9
                    chars[left] = c
                    left += 1
        chars[:] = chars[:left]
        print(chars)
        return len(chars)
        
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)
        ans = [chars[0]]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count > 1:
                    for j in str(count):
                        ans.append(j)
                ans.append(chars[i])
                count = 1
        if count > 1:
            for j in str(count):
                ans.append(j)
        chars[:] = ans
        return len(ans)
