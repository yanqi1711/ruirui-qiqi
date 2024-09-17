class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        pre, cur = 1,2
        res = 0
        for i in range(3,n+1):
            res = pre + cur
            pre = cur
            cur = res
        return res