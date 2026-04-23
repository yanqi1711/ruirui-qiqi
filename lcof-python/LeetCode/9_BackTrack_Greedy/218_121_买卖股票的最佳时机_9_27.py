class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这里的 dp 是一个列表，用来存储目前为止的最低买入价格
        # 下面是贪心算法 dp是二维数组，dp[i][0]表示第i天持有，dp[i][1]表示第i天未持有
        dp = [prices[0]]
        val = 0
        for i in range(1, len(prices)):
            if prices[i] < dp[-1]:
                dp.pop()
                dp.append(prices[i])
            else:
                val = max(val, prices[i]-dp[-1])
        return val
