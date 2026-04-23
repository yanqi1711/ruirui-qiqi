from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 删除操作 + 统计子序列个数
        m,n = len(s), len(t)
        mod = 10 ** 9 + 7
        # s的[0:i]个字符 能够组成dp[i][j]个t[0:j] 注意:增加了空串的情况
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        #  空串自己组成空串
        dp[0][0] = 1
        # 初始化行
        for i in range(1, m+1):
            # s中能够组成多少空串 注:编辑距离中的删除操作类似
            dp[i][0] = 1
        # 列的初始化为0 在创建dp时就已经完成
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    # 选择s[i-1]能够组成多少t[:j] + 不选择s[i-1](之前的已经存在的子序列的数量)
                    # 选择s[i-1]时 之前的已经计算过了 
                    # 因为dp[i-1][j-1] 之前已经通过 dp[i-1][j] 加上了之前的情况
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
                else:
                    #  不等于 说明自身不能组成子序列 只能用自身之前的情况
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

# 递归写法
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 删除操作 + 统计子序列个数
        m,n = len(s), len(t)
        mod = 10 ** 9 + 7
        @cache
        def dfs(i, j):
            # 相当于初始化
            # i小于j永远无法组成
            if i < j:
                return 0
            if j < 0:
                # t 为空串 肯定可以组成一个空串
                return 1
            if s[i] == t[j]:
                return (dfs(i-1, j-1) + dfs(i-1, j)) % mod
            return dfs(i-1, j)
        return dfs(m-1, n-1)