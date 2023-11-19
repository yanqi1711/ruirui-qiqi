class Solution:
    # 累加和小于0 就从下一个重新开始
    def FindGreatestSumOfSubArray(self , array: List[int]) -> int:
        # write code here
        max = 0
        result = array[0]
        for i in range(len(array)):
            max += array[i]
            # 为什么必须在max < 0的前面呢 -> -1 -2 -3
            if max > result:
                result = max
            # 累加和为负数 从下一个开始
            if max < 0: max = 0
        return result

        # 动态规划解法
        #记录到下标i为止的最大连续子数组和
        # dp = [0 for i in range(len(array))]
        # dp[0] = array[0]
        # maxsum = dp[0]
        # for i in range(1, len(array)):
        #     #状态转移：连续子数组和最大值
        #     dp[i] = max(dp[i - 1] + array[i], array[i])
        #     #维护最大值
        #     maxsum = max(maxsum, dp[i])
        # return maxsum