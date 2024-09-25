class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:return 0
        n = len(s)
        # 状态定义:当前字符结尾最长连续括号
        dp = [0 for _ in range(n)]
        maxVal = 0
        # 第一个不管是哪一个肯定是0
        for i in range(1, n): 
            if s[i] == ")": 
                # 防止i - dp[i-1] -1小于0 越界
                # and 之后 减去前一个匹配好了的长度然后去找和当前')'匹配的"("
                if i - dp[i-1] > 0 and s[i-dp[i-1]-1] == "(":
                    # 1 直接(括号匹配上了就占2个)+2 
                    # 2 被当前括号包围的情况->之前已经匹配过的dp[i-1]
                    # 3 当前匹配完之后 之前是否匹配 因为可能被当前的"(" 遮挡 ()(())
                    dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
                maxVal = max(maxVal, dp[i])
        return maxVal
    