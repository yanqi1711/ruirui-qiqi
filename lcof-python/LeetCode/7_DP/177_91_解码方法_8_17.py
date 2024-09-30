class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [ 0 for _ in range(n)]
        dp[0] = 1
        # 每到一个字母都有两个可解码状态 [第一个除外 所以dp[0] = 1]
        for i in range(1, n):
            # 自己单独就可以解码的状态 n种状态 + 1个字符
            if s[i] != '0': dp[i] += dp[i-1]
            # 和前面的一个组成解码状态 n-1状态 + 2个字符(组成一个码)
            if s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6':
                if i-2 >= 0: # 前面有可组合的
                    dp[i] += dp[i-2]
                else: # i=2时 只有自己
                    dp[i] += 1
        return dp[-1]