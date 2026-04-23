class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        flag = True
        # dp[0][0] 是开始位置 开始位置是障碍物直接返回0
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        for i in range(1,m):
            # 把有石头的地方无法到达 为0 改变所有有石头的地方
            if obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = 0
                # 改变flag 因为初始化 从上往下有一个石头 剩下的都到不了
                flag = False
                continue
            if flag:
                obstacleGrid[i][0] = 1
        flag = True
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                obstacleGrid[0][j] = 0
                flag = False
                continue
            if flag:
                obstacleGrid[0][j] = 1
        # 开始进行dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
        print(obstacleGrid)
        return obstacleGrid[-1][-1]