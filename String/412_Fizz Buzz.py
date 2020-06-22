class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 5 == 0:
                ans.append("Buzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            num_str = ""
            if i % 3 == 0:
                num_str += "Fizz"
            if i % 5 == 0:
                num_str += "Buzz"
            if not num_str:
                num_str = str(i)
            ans.append(num_str)
        return ans
        
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        dict = {3 : "Fizz", 5 : "Buzz"}
        for i in range(1, n+1):
            num_str = ""
            for key in dict.keys():
                if i % key == 0:
                    num_str += dict[key]
            if not num_str:
                num_str = str(i)
            ans.append(num_str)
        return ans
