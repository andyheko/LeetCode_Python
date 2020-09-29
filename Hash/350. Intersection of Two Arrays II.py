class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): # keep nums1 shorted
            return self.intersect(nums2, nums1)

        set1 = Counter(nums1) # count nums1
        i = 0 # index refer to the len of ans
        for num2 in nums2: # scan nums2
            cnt = set1.get(num2, 0)
            if cnt > 0:
                nums1[i] = num2
                i += 1
                set1[num2] = cnt-1 # decrease the count in set1
        return nums1[:i]
