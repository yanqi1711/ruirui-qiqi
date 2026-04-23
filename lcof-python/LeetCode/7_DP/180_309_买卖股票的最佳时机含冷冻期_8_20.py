class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0]: 买  当天 不买和买 两种情况
        # dp[i][1]: 卖  卖或者不卖
        # dp[i][2]: 冷冻
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])   买的话需要之前非冷冻期并且卖掉之前的状态
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[0])
        # dp[i][2] = dp[i-1][1] 冷冻期 得到的钱就是之前卖出的
        # 最后结果 max(dp[i][1], dp[i][2]) 因为最后一天还有没卖出去的 一定亏本
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+prices[0])
            dp[i][2] = dp[i-1][1]
        return max(dp[n-1][1], dp[n-1][2])