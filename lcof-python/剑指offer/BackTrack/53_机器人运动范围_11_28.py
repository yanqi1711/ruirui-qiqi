class Solution:
    def cal(self,num):
        sum_value = 0
        while num:
            sum_value += (num % 10)
            # 必须整除
            num //= 10
        return sum_value

    def dfs(self, threshold, rows, cols, i, j, flag_matrix):
        if i < 0 or i >= rows or j < 0 or j >= cols \
            or self.cal(i) + self.cal(j) > threshold \
            or flag_matrix[i][j]:
            return 0
        flag_matrix[i][j] = True
        # 开始扩散
        return 1 + self.dfs(threshold, rows, cols, i - 1, j, flag_matrix) \
               + self.dfs(threshold, rows, cols, i + 1, j, flag_matrix) \
               + self.dfs(threshold, rows, cols, i, j - 1, flag_matrix) \
               + self.dfs(threshold, rows, cols, i, j + 1, flag_matrix)
        

    def movingCount(self , threshold: int, rows: int, cols: int) -> int:
        # write code here
        if (rows <= 0 or cols <= 0 or threshold < 0):
            return 0
        flag_matrix = [[False for i in range(cols)] for j in range(rows)]
        count = self.dfs(threshold, rows, cols, 0, 0, flag_matrix)
        return count