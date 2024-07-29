from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m,n = len(matrix),len(matrix[0])
        l,r = 0, m*n-1
        while l <= r:
            mid = (l+r) >> 1
            row,col = mid // n , mid % n
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    print(s.searchMatrix(matrix,3))