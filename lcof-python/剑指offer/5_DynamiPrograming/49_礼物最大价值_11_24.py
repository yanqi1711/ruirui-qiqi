class Solution:
    def maxValue(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        # 原数组就是dp数组 可以直接在原数组修改 直接省略dp数组步骤创建过程
        for j in range(1, n):
            grid[0][j] = grid[0][j - 1] + grid[0][j]
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i][j] + max(grid[i-1][j], grid[i][j-1])
        print(grid)
        return grid[m-1][n-1]
    
if __name__ == "__main__":
    s = Solution()
    s.maxValue([[1,3,1],[1,5,1],[4,2,1]])
    