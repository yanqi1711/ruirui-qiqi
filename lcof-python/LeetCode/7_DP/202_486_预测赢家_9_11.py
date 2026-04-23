class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        # 代表i到j之间拥有优先权得到的最大分数 所以最后结果是dp[0][-1]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-1, -1, -1): # 从下往上
            for j in range(i+1, n): # 从左到右
                # 选择i和选择j能相差多少 取最大值 也就是找全全局最优
                # 选择i就要丢掉j的选择权, 这就是对于优先的选择图
                # 对于唯一的i而言:选择了j就会失去之前j-1的权利 而dp[i][j-1]标记的就是之前 i到j-1先手能拿到的最大分数差
                # 词语选择j的话就失去了优先权 就必须和之前的i+1到j的最大值比(此时是对手优先)
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return True if dp[0][-1] >= 0 else False