class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0

        left = right = 0
        max_len = 1
        hashmap = {} # {s[idx]: idx}

        while right < len(s):
            hashmap[s[right]] = right

            if len(hashmap) > k:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k == 0:
            return 0

        left = right = 0
        max_len = 1
        hashmap = OrderedDict() # {s[idx]: idx}

        while right < len(s):
            if s[right] in hashmap:
                del hashmap[s[right]]
            hashmap[s[right]] = right

            if len(hashmap) > k:
                # delete the leftmost character
                _, del_idx = hashmap.popitem(last = False)
                left = del_idx + 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
