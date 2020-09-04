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
