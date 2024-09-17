class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        for _ in range(n):
            a,b=b,b+a
        return a
class Solution:
    # 二阶其实可以加速
    def mutiply(self, matrix1, matrix2):
        # 总结果数
        res = []
        for i in range(len(matrix1)): # 行数
            # 第
            temp = []
            for j in range(len(matrix2[0])): # 列数
                sum_ = 0
                # 结果计算每一个值 
                for k in range(len(matrix2)): # 
                    sum_ += matrix1[i][k] * matrix2[k][j]
                # 每一行加上结果 持续(列的大小)次
                temp.append(sum_)
            res.append(temp)
        return res

    def matrix_quickpow(self, matrix, n:int):
        M = [[0,1], [1,1]]
        while n > 0:
            if n & 1 == 1:
                matrix = self.mutiply(M, matrix)
            n = n >> 1
            M = self.mutiply(M , M)
        return matrix

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        matrix = [[1],[1]]
        result = self.matrix_quickpow(matrix, n-1)
        return result[0][0]