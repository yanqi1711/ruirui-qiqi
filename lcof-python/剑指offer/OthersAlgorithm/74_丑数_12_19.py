class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        if index == 0:
            return 0
        dp = [1 for _ in range(index)]
        a, b, c = 0, 0, 0
        for i in range(1, index):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
            if dp[i] == dp[a] * 2:
                a += 1
            if dp[i] == dp[b] * 3:
                b += 1
            if dp[i] == dp[c] * 5:
                c += 1
        print(dp)
        return dp[-1]