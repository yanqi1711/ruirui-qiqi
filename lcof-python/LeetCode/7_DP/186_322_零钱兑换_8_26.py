class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:  # 当 amount 为 0 时，直接返回 0
            return 0
        if not coins or amount < 0:  # 没有硬币或者金额为负时返回 -1
            return -1
        # 当前dp[i] 满足amout的最少次数
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i- coins[j]]+1)
        # 不符合情况 说明没找到最小值 返回-1
        return -1 if dp[amount] > amount else dp[amount]