from bisect import bisect_left
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i, interval in enumerate(intervals):
            # 索引记录 原来的位置
            interval.append(i)
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)
        ans = [-1] * n
        for _, end, rowIndex in intervals:
            # 可以插入end的地方就是原列表之后的地方
            i = bisect_left(intervals, [end])
            if i < n:
                # 第二个就是原来的索引
                ans[rowIndex] = intervals[i][2]
        return ans
