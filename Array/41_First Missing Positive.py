def firstMissingPositive(self, nums: List[int]) -> int:
    i = 0
    n = len(nums)
    # put nums[i] in correct place if 1 <= nums[i] <= n
    while i < n:
        j = nums[i] - 1
        if 0 <= j < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # find out which place is wrongly occupied
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
