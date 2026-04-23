from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = -1, -1  # 初始化为-1表示未找到无序部分
        max_seen, min_seen = float('-inf'), float('inf')
        
        # 从左到右扫描，找到右边界
        for i in range(n):
            # 左到右看，数应该越来越大，如果小于前面的最大值，那么这个数就有问题
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]
        
        # 从右到左扫描，找到左边界
        for i in range(n - 1, -1, -1):
            # 同理
            if nums[i] > min_seen: 
                start = i
            else:
                min_seen = nums[i]
        
        # 如果未找到无序部分，返回0，否则返回子数组长度
        return 0 if start == -1 else end - start + 1
