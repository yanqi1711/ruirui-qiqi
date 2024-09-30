class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        x2 = x3 =x5 = 0
        for i in range(1, n): 
            #  num1,num2,num3 = x2*2, x3*3, x5*5 会出现2*7=14
            # 因为dp数组内部都是2 3 5的因子 他们乘以2 3 5一定也是合理的序列
            # 已计算的丑陋数列表中获取值
            num1,num2,num3 = dp[x2]*2, dp[x3]*3, dp[x5]*5
            dp[i] = min(num1, num2, num3)
            if dp[i] == num1:
                x2 +=1
            if dp[i] == num2:
                x3 += 1
            if dp[i] == num3:
                x5 += 1
        print(dp)
        return dp[-1]