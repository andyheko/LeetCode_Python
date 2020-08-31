class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        def twoSumSmaller(nums, startIndex, target):
            count = 0
            left = startIndex
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    count += right - left # plus combinations between right, left
                    left += 1
                else:
                    right -= 1
            return count
        count = 0
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            count += twoSumSmaller(nums, i + 1, target - nums[i])
        return count

def closest(s, arr queries):
	n = len(s)
	output = [0] * len(queries)
	map = {}
	for i in n:
		if s[i ]in map:
			map[s[i]].append(i)
		else:
			map[[s[i]] = [i]
	for j, index in enumerate(queries):
		if len(map[s[index]]) == 1
			output[j] = -1
		else:
			left, right = 0, len(map[s[index]])-1
			while left < right:
				mid = (left + right) // 2
				if map[s[index]][mid] == index:
                    if mid == 0:
                        output[j] = map[s[index]][1]
                    elif mid == len(map[s[index]]) - 1:
                        output[j] = map[s[index]][1]
                    else:
                        if map[s[index]][mid] - map[s[index]][mid-1] <= map[s[index]][mid+1] - map[s[index]][mid]:
                            output[j] = map[s[index]][mid-1]
                        else:
                            output[j] = map[s[index]][mid+1]
                elif map[s[index]][mid] > index:
                    right = mid - 1
                else:
                    left = mid + 1
			output[j] =
