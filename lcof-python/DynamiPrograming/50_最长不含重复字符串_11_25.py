class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = len(s)
        dp = [1 for i in range(m)]
        mp = dict()
        res = 1
        mp[s[0]] = 0
        for i in range(1, m):
            if s[i] not in mp:
                dp[i] = dp[i - 1] + 1
            else:
                # 如果越界就还是dp = dp+1 如果没有越界还是在范围内 就i-k是两个之间的差值
                dp[i] = min(dp[i-1] + 1,i - mp[s[i]])
            mp[s[i]] = i
            res = max(res, dp[i])
        return res
        # 双重循环
        # for i in range(1, m):
        #     flag = False
        #     temp = 0
        #     # 优化 使用哈希存储下标 但是需要判断是否越界
        #     # 哈希需要不断更新最近的下标
        #     for j in range(dp[i-1],0,-1):
        #         if s[i] == s[i - j]:
        #             temp = 0
        #             flag = True
        #         else:
        #             temp += 1 
        #     if  flag == False:
        #         dp[i] = dp[i-1] + 1
        #     else:
        #         dp[i] = 1 + temp
        # print(dp)
        # return max(dp)