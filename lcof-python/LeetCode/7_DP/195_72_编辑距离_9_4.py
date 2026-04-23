class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        # '' 代表为空时候需要删除的状态
        # m+1 n+1 需要考虑
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # 当前2个相同 说明不需要操作 等于之前都没有时候需要操作的状态
                    dp[i][j] = dp[i-1][j-1]
                else: # 需要删除一个 来达到之前的平衡状态
                    # dp[i-1][j] 删word1
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)     
        return dp[-1][-1]