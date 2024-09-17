class Solution:
    def cutRope(self , n: int) -> int:
        # # 均值不等式 求 y = x ** (1/x) 的极值 对数求导
        if  n <= 3:
            return n - 1
        res = n // 3
        mod = n % 3
        if mod == 0:
            return 3 ** (res)
        elif mod == 1:
            return (3 ** (res - 1)) * 4
        else:
            return  (3 ** (res)) * 2
        # 动态规划 dp的意义是当前为n的最大值
        # dp = [0 for i in range(n+1)]
        # dp [2] = 1
        # # 2已经知道 现在推导长度为3，4 .... n 时候的最大值
        # for i in range(3,n+1):
        #     # 这里是切与不切的问题 切j留下i-j 或者 不切直接乘
        #     # 切一刀多也就是n-1 所以到i停止
        #     # 只需要找到当前长度切or不切的最大值就可以
        #     for j in range(2,i):
        #         # 第一个max记录最大值 第二个是当前切 or 不切的最大值
        #         dp[i] = max(dp[i], max(j * dp[i-j], j * (i-j)))
        # return dp[n]