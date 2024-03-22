class Solution:
    def __init__(self) -> None:
        self.mod = 998244353

    # 快速乘法 => 乘法变加法
    # 20 * 14 = 20 * (1110) = 280 = 20 * (2^3) + 20 * (2^2) + 20 * (2^1)
    #                                左移3次      左移2次       左移1次
    def fast_multiply(self, n:int, m:int):
        res = 0
        n %= self.mod
        m %= self.mod
        while m:
            if m & 1:
                res += n
                res %= self.mod
            m = m >> 1
            n = n << 1
            n %= self.mod
        return res

    # 快速幂 指数是循环条件 为1就乘 每一次都需要乘以自己
    #  1101 = n^3 * 1 + n ^2 * 1 + n^1 * 0 + n ^0 * 1
    # n就是底数
    def FastPow(self, n: int, exponent: int):
        res = 1
        while exponent:
            if exponent & 1 == 1:
                res = self.fast_multiply(res, n)
            n = self.fast_multiply(n, n)          
            exponent = exponent >> 1
        return res

    def cutRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        res = n // 3
        mod = n % 3
        if mod == 0:
            return self.FastPow(3, res) % self.mod
        elif mod == 1:
            return (self.FastPow(3, res - 1) * 4) % self.mod
        else:
            return (self.FastPow(3, res) * 2) % self.mod