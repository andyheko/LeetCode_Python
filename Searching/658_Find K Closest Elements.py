class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        # goal is make x be at the mid of arr[mid] and arr[mid+k] window
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x: # x is closer to mid+k, move window to right
                left = mid + 1
            else: # x is closer to mid, move window to left
                right = mid
        return arr[left:left + k]
