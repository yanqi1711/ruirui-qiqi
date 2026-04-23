"""
买卖股票的最佳时机 II
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。
你也可以先购买，然后在 同一天 出售.
返回 你能获得的 最大 利润 。

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天(股票价格 = 1)的时候买入,在第 3 天(股票价格 = 5)的时候卖出, 
这笔交易所能获得利润 = 5-1 = 4

prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天(股票价格 = 1)的时候买入,在第 5 天 (股票价格 = 5)的时候卖出,
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心 因为每天都能买卖 画成折线图 所以每次涨幅的收益就是最大利润
        # return sum([ prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0 for i in range(1, len(prices))])
        # 正经做法 dp 和121一样
        # dp是二维数组，dp[i][0]表示第i天持有，dp[i][1]表示第i天未持有
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # dp[0][0]代表持有自然是负数
        dp[0][0] = -prices[0]
        for i in range(1,n):
            # 持有股票的最大值->[昨天的持有的(没有卖), 昨天的未持有的钱减去现在的]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            # 未持有 持有的卖掉了，以及一直未持有
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
        return max(dp[n-1][0],dp[n-1][1])