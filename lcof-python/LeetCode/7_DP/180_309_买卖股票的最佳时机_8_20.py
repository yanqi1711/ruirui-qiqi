class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [prices[0]]
        val = 0
        for i in range(1, len(prices)):
            if prices[i] < dp[-1]:
                dp.pop()
                dp.append(prices[i])
            else:
                val = max(val, prices[i]-dp[-1])
        return val
