class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0:
            return 0
        dp = [0] * (n+1)
        # 0 不能进入循环 表示0个0
        for i in range(1,n+1):
            # i 对应每一个数字 
            # 第二个循环找 之前存在的情况
            minn = n+1
            j = 1
            while j * j <= i:
                # 找到符合挡墙最小的数
                # 3 -> 3个1 
                # 4 -> 2^2 只需要一个 所以直接 减到0了
                minn = min(minn, dp[i - j*j])
                j += 1
            # 之前的需要mins个 现在需要+1
            dp[i] = minn + 1
        return dp[n]