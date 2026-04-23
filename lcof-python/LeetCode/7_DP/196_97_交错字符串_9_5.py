class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool: 
        if not s1 and not s2 and not s3:
            return True
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        # dp定义: s1的前 i 个元素和 s2的前 j 个元素是否能交错组成s3
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        # 初始化 因为相当于给s1 s2增加了空串的情况
        # 当s2为空 s1不为空
        for i in range(1,m+1):
            # 当前状态需要和之前的匹配
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # 初始化相当于已经完成了第一次匹配,相当于从两个之中选一个
        for i in range(1, m+1):
            for j in range(1, n+1):
                # s1 最后一个和 s1[:i-1]与s2[:j] 组成s3 
                # s2 最后一个和 s1[:i]与s2[:j-1] 组成s3 i+j-1就是当前最后一个词
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        print(dp)
        return dp[-1][-1]