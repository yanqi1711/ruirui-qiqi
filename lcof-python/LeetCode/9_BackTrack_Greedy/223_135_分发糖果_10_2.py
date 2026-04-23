class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 满足2个规则
        # 右边比左边大
        # 左边比右边大 2次遍历
        if not ratings:
            return -1
        n = len(ratings)
        dp = [1] * n
        for i in range(1, n): #右边大于左边
            # 右边评分高的孩子获得更多糖果
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1
        # 如果不反向就会无法利用上面的结果
        for i in range(n-2, -1, -1):
            # 保证左边评分高的孩子获得更多糖果
            if ratings[i] > ratings[i+1]:
                # max 保证不覆盖之前的结果
                dp[i] = max(dp[i], dp[i+1] + 1)
        return sum(dp)
