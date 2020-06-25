class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
                }
        result = []

        def helpCombine(current, leftoverDigits):
            if not leftoverDigits: # base case
                return result.append(current)
            else: # recursive case
                for char in phone[leftoverDigits[0]]:
                    helpCombine(current + char, leftoverDigits[1:])


        helpCombine("", digits)
        return result

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if not digits:
            return []
        else:
            self.helpCombine("", digits, result)
        return result


    def helpCombine(self, current, leftoverDigits, result):
        phone = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
                }

        if not leftoverDigits: # base case
            return result.append(current)
        else: # recursive case
            for char in phone[leftoverDigits[0]]:
                self.helpCombine(current + char, leftoverDigits[1:], result)
