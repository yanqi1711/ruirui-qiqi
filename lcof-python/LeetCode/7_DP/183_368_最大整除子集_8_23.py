from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        # 当前最长的子集数 自身一定在里面 所以初始化为1
        dp = [1] * n
        # 记录最大的子集长度 和当前的被除数（当前i的数一定是子集里的最大数
        maxSize = 1
        maxValue = nums[0]

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # dp[j]+1 自身加上新的能除以为0的nums[i]
                    dp[i] = max(dp[i], dp[j] + 1)
            # 更新最大dp长度
            # 更新当前的最大子集所对应最大数
            if dp[i] > maxSize:
                maxSize = dp[i]
                maxValue = nums[i]

        ans = []
        # 开始计算最大子集
        for i in range(n-1,-1,-1):
            # maxSize <= n
            if maxSize <= 0:
                return ans
            if dp[i] == maxSize and maxValue % nums[i] == 0: # 可能长度相等
                ans.append(nums[i])
                maxValue = nums[i]
                maxSize -= 1
        return ans