class Solution:
    # n 矩阵行 m 矩阵列
    # i j 当前位置
    # word 单词 k 判断当前单词的位置
    # flag_matrix 判断是否已经访问
    def dfs(self, matrix, n, m, i, j, word, k, flag_matrix ):
        if i<0 or i>=n or j<0 or j>=m or(matrix[i][j] != word[k]) or flag_matrix[i][j]:
            return False
        # 是否结束
        if k == len(word) - 1:
            return True
        
        # 匹配 设置为False
        flag_matrix[i][j] = True

        # 开始扩散
        if self.dfs(matrix, n,m,i-1,j,word,k+1,flag_matrix) \
            or self.dfs(matrix, n,m,i+1,j,word,k+1,flag_matrix) \
            or self.dfs(matrix, n,m,i,j-1,word,k+1,flag_matrix) \
            or self.dfs(matrix, n,m,i,j+1,word,k+1,flag_matrix):
            return True
        # 前面匹配 但是后面不匹配 需要设置为False
        flag_matrix[i][j] = False
        return False

    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        flag_matrix = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if self.dfs(matrix, n, m, i, j,word, 0,flag_matrix):
                    return True
        return False