class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 确定问题 01背包
        if m <0 and n <0:
            return 0
        # 全部初始化为0
        # 表示i个0和j个1时候的状态
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        from collections import Counter
        for s in strs:
            # 找到数量的0和1
            number = Counter(s)
            # 压缩到二维
            # 先物品 后背包
            print(number)
            if number['0'] > m or number['1'] > n:
                continue
            for i in range(m, number['0']-1, -1):
                for j in range(n, number['1']-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-number['0']][j-number['1']] +1)
        print(dp)
        return dp[m][n]
