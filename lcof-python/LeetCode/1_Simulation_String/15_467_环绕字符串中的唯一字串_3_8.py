"""
467. 环绕字符串中唯一的子字符串
定义字符串 base 为一个 "abcdefghijklmnopqrstuvwxyz" 无限环绕的字符串，所以 base 看起来是这样的：

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
给你一个字符串 s ，请你统计并返回 s 中有多少 不同非空子串 也在 base 中出现。
"""

class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # dp含义: 每个字母所对应的最多子串数 最大字串包含小子串
        dp = [0] * 26
        # 定义连续个数
        count = 0
        for i in range(len(s)):
            # 记录每次连续时字串所包含的数量
            if i > 0 and ((ord(s[i]) - ord(s[i-1]) + 26) % 26) == 1:
                count += 1
            else:
                count = 1
            # 因为字符出现不止一次 记录最大字串时 自动去重
            dp[ord(s[i]) - 97] = max(count, dp[ord(s[i]) - 97])
        return sum(dp)