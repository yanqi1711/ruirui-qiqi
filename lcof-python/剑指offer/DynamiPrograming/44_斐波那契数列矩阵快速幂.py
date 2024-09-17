class Solution:
    # acm 不能用numpy
    def mutiply(self, matrix1, matrix2):
        res = []
        for i in range(len(matrix1)):
            temp = []
            for j in range(len(matrix2)):#3*4 4*3 不能加[1] 这里运气好 都是2,2 换一个就寄
                sum = 0
                for k in range(len(matrix2)):
                    sum += matrix1[i][k] * matrix2[k][j]
                temp.append(sum)
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
            
    def Fibonacci(self , n: int) -> int:
        # write code here
        # 矩阵快速幂
        if n < 2:
            return n
        matrix = [[1],[1]]
        result = self.matrix_quickpow(matrix, n-1)
        return result[0][0]