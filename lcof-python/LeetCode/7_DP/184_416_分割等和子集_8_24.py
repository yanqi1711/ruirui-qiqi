class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        sum_ = sum(nums)
        target = sum_ / 2
        if (sum_ & 1) or (max(nums) > target):
            return False
        target = int(target)
        # 因为是从0->target 需要加1
        # 乘法符号 * 来创建二维列表，这会导致所有的行引用到同一个列表
        dp = [[False for _ in range(target + 1)]  for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target+1):
                if j < nums[i]:
                    # dp[i]取不到的值 之前的可以得到
                    dp[i][j] = dp[i-1][j]
                else:
                    # 不取 |  取值 有一个满足条件就行 
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[n-1][target]
