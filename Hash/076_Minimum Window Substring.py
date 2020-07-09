class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t) # {'A': 1, 'B': 1, 'C': 1}
        required = len(dict_t)
        current = 0 # keep track of how many required items are in current
        r = l = 0
        current_window = {} # contain current item and count
        ans = (float("inf"), l, r) # store min length, left index, right index

        while r < len(s):
            current_window[s[r]] = current_window.get(s[r], 0) + 1
            if s[r] in dict_t and current_window[s[r]] == dict_t[s[r]]:
                current += 1
            # while requied is formed
            while current == required and l <= r:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                current_window[s[l]] -= 1
                if s[l] in dict_t and current_window[s[l]] < dict_t[s[l]]:
                    current -= 1
                l += 1

            r += 1

        return s[ans[1] : ans[2] + 1] if ans[0] != float("inf") else ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t) # {'A': 1, 'B': 1, 'C': 1}

        filtered_s = []
        for i, c in enumerate(s):
            if c in dict_t:
                filtered_s.append((i, c))

        required = len(dict_t)
        current = 0 # keep track of how many required items are in current
        r = l = 0
        current_window = {} # contain current item and count
        ans = (float("inf"), l, r) # store min length, left index, right index

        while r < len(filtered_s):
            character = filtered_s[r][1]
            current_window[character] = current_window.get(character, 0) + 1
            if current_window[character] == dict_t[character]:
                current += 1
            # while requied is formed
            while current == required and l <= r:
                character = filtered_s[l][1]
                rr = filtered_s[r][0]
                ll = filtered_s[l][0]
                if rr - ll + 1 < ans[0]:
                    ans = (rr - ll + 1, ll, rr)
                current_window[character] -= 1
                if character in dict_t and current_window[character] < dict_t[character]:
                    current -= 1
                l += 1

            r += 1

        return s[ans[1] : ans[2] + 1] if ans[0] != float("inf") else ""
