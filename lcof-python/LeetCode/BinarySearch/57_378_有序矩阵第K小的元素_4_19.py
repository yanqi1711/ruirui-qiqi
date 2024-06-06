from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # n*n 矩阵
        n = len(matrix)
        # 划分 检查有多少个是左边的 从左下角开始 因为 左下角小于mid 那么前面都小于
        def check(mid):
            i,j = n-1,0
            # 检测
            count = 0
            while i >= 0 and j < n:
                # 先计算列
                if matrix[i][j] <= mid:
                    count = count + i + 1
                    # 向右扩张
                    j+=1
                else:
                    i-=1
            return count >= k
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

