class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c : i for i, c in enumerate(S)} # record {char : last index}
        left = right = 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, rightmost[c]) # *** the last index of each part
            if i == right:
                ans.append(i-left+1)
                left = i + 1
        return ans
