class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        # dp表示以i为结尾的最大连续子数组和
        dp = [0] * n
        dp[0] = nums[0]
        # maxAns = nums[0]
        for i in range(1, n):
            # 1,要之前的和 2，不要之前的 另起炉灶
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            # maxAns = max(maxAns, dp[i])
        # 因为没有记录最大值
        return max(dp)
        """
        二维dp 冗余了
        """
        # dp = [[0,0] for _ in range(n)]
        # # dp[i][0]表示不加入当前前数之前的最大数组和
        # # dp[i][1]表示加入当前数字的最大和
        # # 因为必须至少要有一个元素 其余的都是从这个状态推导出来 所以其余的初始化并不重要
        # dp[0][0] = dp[0][1] = nums[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        #     dp[i][1] = max(nums[i], dp[i-1][1] + nums[i])
        # return max(dp[-1][0], dp[-1][1])