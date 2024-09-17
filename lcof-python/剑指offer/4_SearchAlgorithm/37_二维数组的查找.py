# -*- coding: utf-8 -*-
"""
在一个二维数组array中 每个一维数组的长度相同每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序
请完成一个函数输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
[
[1,2,8,9],
[2,4,9,12],
[4,7,10,13],
[6,8,11,15]
]
"""
class Solution:
    # 二分查找
    def binsearch(self, data, k):
        left, right = 0, len(data) - 1
        # 第一种写法 left <= right 判定等于
        while left <= right:
            mid = (left + right) // 2
            # 重新划分边界 从mid开始
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right =  mid - 1
            else:
                return True
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        # m+n 常数级别
        if not array:
            return False
        row_length = len(array)
        col_length = len(array[0])
        i = row_length - 1
        j = 0
        # 开始找 避免出界 
        # 左下角 比它大的在右边 比它小的在上面
        while i >= 0 and j < col_length:
            if array[i][j] < target:
                j += 1
            elif array[i][j] > target:
                i -= 1
            else:
                return True
        return False

        # 每一层二分查找 nlogn
        # for i in array:
        #     if self.binsearch(i,target) == True:
        #         return True
        #     else:
        #         continue
        # return False
    