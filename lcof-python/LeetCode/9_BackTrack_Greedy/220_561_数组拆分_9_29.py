"""
给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
返回该 最大总和 。
"""
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans += min(nums[i], nums[i+1])
        return ans