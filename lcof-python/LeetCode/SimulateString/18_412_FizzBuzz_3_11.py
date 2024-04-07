class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        # length = len(n)
        for i in range(1, n+1):
            result.append(str(i))
        print(result)
        for j in range(3, n+1,3):
            result[j-1] = "Fizz"
        for j in range(5, n+1,5):
            result[j-1] = "Buzz"
        for j in range(15, n+1,15):
            result[j-1] = "FizzBuzz"
        return result