# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right = 0, n
        while left <= right:
            m = (left +right) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                left = m+1
            else:
                right = m-1
        return -1