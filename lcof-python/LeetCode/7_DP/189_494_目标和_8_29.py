class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        # 01 背包 先物品 然后倒序遍历
        sum_ = sum(nums)
        # 奇数就代表无法组成
        if (sum_+target) & 1 or (sum_+target)<0:
            return 0
        # 物品容量就是其中所有正数集合(负数也可以) 因为是互斥的 不是+号就是-号
        # capacity + sub = sum(nums) 1
        # capacity - sub = target 2
        # capacity + (capacity - target) = sum(nums) 把2带入1
        # capacity = (sum(nums) + target) // 2
        capacity = (sum_ + target) // 2
        # 找多少个 正数集合 就是 '+'号
        # dp表示满足capacity 具有多少种情况
        dp = [0 for i in range(capacity+1)]
        # 必须为1 为了符合后面的情况 如果是回溯是指数级复杂度 2**0 = 1
        dp[0] = 1
        # 遍历nums 遍历到最后一个dp计算完毕
        for num in nums:
            # 找到当前num可以获得多少个
            # 倒序遍历
            for j in range(capacity, num-1, -1):
                # 当前capacity满足多少种情况
                dp[j] += dp[j-num]
        return dp[-1]