class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while end > start:
            sum = numbers[start] + numbers[end]
            if target == sum:
                return [start+1, end+1]
            elif target > sum:
                start += 1
            else:
                end -= 1
