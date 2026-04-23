class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        # 参考516最长回文子序列 486预测赢家
        dp = [[0 for _ in range(n)] for i in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1 # 自己肯定需要一次
            for j in range(i+1, n):
                # 相同就和前面的一样(前面此时可能和当前不一样,但是因为和nums[i]一样在第一次的时候就直接被刷了)
                if s[i] == s[j]: dp[i][j] = dp[i][j-1]
                else: #需要找之前最小次数相加 
                    minn = n+1
                    for k in range(i,j): #i和j不同 计算刷新次数自然要加入自己
                        # [i,k]和[i+k,j]拼起来了一个字符串
                        # 这个循环就是找j前面n个从哪里开始断开并打印字母能取得更小的次数
                        # 本质找 [a bcc] [ab cc] [abc c]之前哪一种次数最少
                        #   a b c c -->不断找当前列下面的次数 因为前面的多了 后面的次数就少了
                        # a 1  
                        # b 0 1 2 2---> (1+1) < (2+1) dp[1][1]+dp[2][3] < dp[1][2] + dp[2][3]
                        # c 0 0 1 1
                        # c 0 0 0 1
                        minn = min(minn, dp[i][k] + dp[k+1][j])
                    dp[i][j] = minn 
        return dp[0][-1]