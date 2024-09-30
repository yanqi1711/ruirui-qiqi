from bisect import bisect_left
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # 从 1, m*n开始找
        # x // n * n 计算钱 i-1层个数 
        # bisect.bisect和bisect.bisect_right返回大于x的第一个下标
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))