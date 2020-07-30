class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        l = [0] * n # store left max for element i
        r = [0] * n # store right max for element i
        ans = 0
        for i in range(n): # build l
            if i == 0:
                l[i] = height[i]
            else:
                l[i] = max(l[i-1], height[i])
        for i in range(n-1, -1, -1):# build r
            if i == n-1:
                r[i] = height[i]
            else:
                r[i] = max(r[i+1], height[i])
        for i in range(n): # cal. ans
            ans += min(r[i], l[i]) - height[i]

        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            # keep left_max and right_max the maximum
            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]
            # ++ans
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
