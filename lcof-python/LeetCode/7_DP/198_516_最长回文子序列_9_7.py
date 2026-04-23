class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 最长括号
        m = len(s)
        # i=0 j = s.length-1 
        # dp表示 i,和j中间包含的回文串的最长长度
        dp = [[0 for _ in range(m)] for i in range(m)]
        # 自身和自己肯定构成回文串
        for i in range(m):
            dp[i][i] = 1
        # 当 s[i] == s[j] dp[i][j] = dp[i+1][j-1] +2->左下角
        # 当 s[i] != s[j] dp[i][j] = max(dp[i][j-1], dp[i+1][j]) 左边和下边
        # 综上 所以需要从最后一行向上遍历 并且j必须一直处于i的右边 i < j
        for i in range(m-1, -1, -1):
            for j in range(i+1, m):
                if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] +2
                else: dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]