class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<0 or n <0:
            return -1
        dp =[[0  for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]