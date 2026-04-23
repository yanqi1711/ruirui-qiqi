class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not coins:
            return -1
        dp = [0] * (amount+1)
        # 需要满足0时 肯定为1种 都不取 
        dp[0] = 1
        # 遍历所有硬币 找到所有硬币可以到达的金额情况
        for coin in coins:
            # 找到当前coin 可以满足的情况
            # coins = [2,3] amount=3
            # 第一个循环 本质是找到硬币为2时 达到其他金额的情况. 比如dp[3] 3由1和2组成,现在选了一次硬币2，所以需要找到dp[1]种选法组合
            # dp[2] = dp[0] 取一个2 
            # dp[3] = dp[1] -coin 是因为此时选择的是coin硬币为2的情况 但是想要金额到达3 需要得到金额为1时的取法数量。此时dp[1] = 0 所以没有这种组合
            # 第二个
            # dp[3] = dp[3-3=0] = 1
            for j in range(coin, amount+1): # 循环中拿到以前的dp[i]金额时的情况
                dp[j] += dp[j-coin]
        return dp[amount]