class Solution:
    def maxProfit(self , prices) -> int:
        # 贪心
        if len(prices) == 1:
            return 0
        # 最后一天只能卖
        min_price = min(prices[-2::-1])
        print(min_price)
        max_price = max(prices[prices.index(min_price) :])
        print(prices.index(min_price))
        return max_price - min_price
class Solution2:
        def __init__(self) -> None:
            pass
        def maxProfit(self, prices):
            dp = [[0 for i in range(2)] for j in range(len(prices))]
            dp[0][0] = -prices[0]
            dp[0][1] = 0
            i = 1
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i-1][0], -prices[i])
                dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
            print(dp)
            return dp[len(prices)-1][1]

if __name__ == "__main__":
     s = Solution2()
     s.maxProfit([8,9,2,5,4,7,1])