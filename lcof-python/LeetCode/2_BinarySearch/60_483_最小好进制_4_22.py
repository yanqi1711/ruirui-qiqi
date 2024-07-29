import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        # 换底公式
        mMax = int(math.log(n) // math.log(2))
        for m in range(mMax,1,-1):
            # k必须是正整数
            k = int(math.pow(n, (1.0/m)))
            print(m ,k)
            # 开始检查 total == n
            total = 1
            multiply = 1
            # 1 k^1 k^2 .... k^(m-1)
            for i in range(m):
                multiply *= k
                total += multiply
            if total == n:
                return str(k)
        # 无论如何都有解 10000 (10000-1)进制
        return str(n-1)