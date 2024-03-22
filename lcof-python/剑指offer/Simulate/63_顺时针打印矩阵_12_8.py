class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        m = len(matrix)
        n = len(matrix[0])
        sum = n * m
        if m == 1 and n != 0: 
            return matrix[0]
        if n == 1:
            for index in range(m):
                res.append(matrix[index][0])
            return res
        i,j = 0,0
        circle = 0
        left,right,upper,lower = 0,0,0,0
        while True:
            while right < n - 1:
                res.append(matrix[i][j])
                sum -= 1
                j += 1
                right += 1
            if sum == 0:
                break
            while lower < m - 1:
                res.append(matrix[i][j])
                sum -= 1
                i += 1
                lower += 1
            if sum == 0:
                break
            while left < n - 1:
                res.append(matrix[i][j])
                sum -= 1
                j -= 1
                left += 1
            if sum == 0:
                break
            while upper < m - 1:
                res.append(matrix[i][j])
                sum -= 1
                i -= 1
                upper += 1
            if sum == 0:
                break
            circle += 1
            i,j = circle,circle
            m , n = m-2, n-2
            left,right,upper,lower = 0,0,0,0
            
            if m == 1:
                while(sum):
                    res.append(matrix[i][j])
                    sum -= 1
                    j += 1
            if n == 1:
                while(sum):
                    res.append(matrix[i][j])
                    sum -= 1
                    i += 1
            if sum == 0:
                break
        return res