class Solution:
    def Power(self , base: float, exponent: int) -> float:
        res = 1
        if exponent < 0:
            base = 1/base
            exponent = -exponent
        while(exponent):
            if exponent&1 == 1:
                res *= base
            base *= base
            exponent >>= 1
        return res