class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return "0"
        comp = lambda a, b: 1 if a+b<b+a else -1 if a+b>b+a else 0
        return "".join(sorted(map(str, nums), key=cmp_to_key(comp))).lstrip('0') or "0"

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)-1, 0, -1): # start from len(nums)-1 to 1
            for j in range(i):
                if not self.compare(nums[j], nums[j+1]): # if n1+n2 < n2+n1
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))  # "00" becomes "0"
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
