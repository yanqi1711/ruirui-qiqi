class Solution:
    def match(self , str: str, pattern: str) -> bool:
        # write code here
        if str == None and pattern == None:
            return True
        if pattern == None or str == None:
            return False
        n = len(str)
        m = len(pattern)
        dp = [[False for i in range(m+1)] for j in range(n+1)]
        # dp[i][j] 当字符串长度为ij时 s与p是否匹配
        dp[0][0] = True
        for j in range(2,m+1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, n+1):
            for j in range(1, m+1):
                # 第一个字符一定不是* 
                # 判断是否为*  不是就进入下一层
                if pattern[j - 1] != '*':
                    # 判断是否为. 或者匹配 进入状态转移方程
                    if pattern[j - 1] == '.' or str[i-1] == pattern[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # 第j-1个是否与str相等
                    # dp数组从0个字符开始 但是pattern从1个字符开始 故索引相差1
                    # 先判断pattern[j-2] == str[i-1]
                    if pattern[j-2] != str[i-1] and pattern[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    else:
                        # 匹配0个 匹配1个 匹配n个
                        dp[i][j] = dp[i][j-2] or dp[i][j-1] or dp[i-1][j]
        return dp[n][m]