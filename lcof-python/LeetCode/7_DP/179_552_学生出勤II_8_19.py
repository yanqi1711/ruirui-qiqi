class Solution:
    def checkRecord(self, n: int) -> int:
        if n <= 0:
            return 0
        mod = 1000000007
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        # dp[i][j][k] j代表A出现的次数 k代表L出现的次数
        # 整个dp代表 当天所有情况
        dp[0][0][0] = 1
        for i in range(1, n+1):
            # P
            for j in range(2): # A出现次数不会被消除 所以j不会变
                for k in range(3): # 迟到次数会被消除为0 所以需要把k情况全部加到 k=0的位置
                    # 基于以上2个原因 所以j会变 k都为0
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k])% mod
            
            # A
            for k in range(3): # A出现的话 只能从前一天0里面取得然后自身j += 1 但是本身会去除L的连续情况
                dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % mod
            
            # L
            for j in range(2): # j是不会变的
                for k in range(1, 3): # k 都需要增加1 从原来k-1变化得来 
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k-1]) % mod
        # 计算最后一个dp的总和就是结果
        ans = 0
        for j in range(2):
            for k in range(3):
                ans = (ans + dp[n][j][k])%mod
        return ans

class Solution:
    mod = 1000000007
    def multiply(self, matrix1, matrix2):
        ans = []
        for i in range(len(matrix1)): # 行
            temp = []
            for j in range(len(matrix2[0])): # 列
                sum_ = 0
                for k in range(len(matrix2)): #计算需要加多少行
                    sum_ += matrix1[i][k] * matrix2[k][j]
                    sum_ %= self.mod
                temp.append(sum_)
            ans.append(temp)
        return ans
    
    def matrixpow(self,mat, n):
        # 初始状态
        cur = [[1, 0, 0, 0, 0, 0]]
        while n>0:
            if n&1 == 1:
                cur = self.multiply(cur, mat)
            n >>= 1
            mat = self.multiply(mat, mat)
        return cur

    def checkRecord(self, n: int) -> int:
        if n <= 0:
            return 0
        
        # dp[j * 3 + k] 0,1,2代表 j=0即不存在A
        # 一共13个变化 出现P:6种 A:3种 L:4种
        # dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2] 这是当前为p时的情况
        # dp[i][1] = dp[i−1][0] L
        # dp[i][2] = dp[i−1][1] L
        # dp[i][3] = dp[i−1][0] + dp[i−1][1] + dp[i−1][2](这是来A的情况) + dp[i−1][3] + dp[i−1][4] + dp[i−1][5] (来P的情况)
        # dp[i][4] = dp[i−1][3] L
        # dp[i][5] = dp[i−1][4] L
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]
        ans = self.matrixpow(mat, n)
        ans = sum(ans[0])
        print(ans)
        return ans % self.mod