class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        step1 = 1
        step2 = 2
        for i in range(3,number + 1):
            result = step1 + step2
            step1 = step2
            step2 = result
        return result