class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2

        def getkth(nums1, m, nums2, n, k):
            if m > n:
                return getkth(nums2, n, nums1, m, k)
            if m == 0: # if nums1 is empty
                return nums2[k-1]
            if k == 1: # if median is the min. of first nums1 or nums2
                return min(nums1[0], nums2[0])

            i = min(m, k//2)
            j = min(n, k//2)
            if nums1[i-1] > nums2[j-1]: # cut off orange area at nums2
                return getkth(nums1, m, nums2[j:], n-j, k-j)
            else:
                return getkth(nums1[i:], m-i, nums2, n, k-i)

        return (getkth(nums1, m, nums2, n, left) + getkth(nums1, m, nums2, n, right)) / 2 # consider both odd & even circumstances
# Time : O(log (m+n))
# Space : O(1)
