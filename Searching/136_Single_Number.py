# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         output = []
#         for i in nums:
#             if i in output:
#                 output.remove(i)
#             else:
#                 output.append(i)
#         return output.pop()

#time:O(n^2)
#space:O(n)

### Use Hash Table
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for i in hash_table:
            if hash_table[i] == 1:
                return i

#time:O(n)
#space:O(n)
