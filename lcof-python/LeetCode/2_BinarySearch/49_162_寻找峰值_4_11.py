from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0,len(nums) - 1
        # 严格大于 左右所以不能等于
        while left < right:
            mid = (left+right) >> 1
            # left < right 所以一定可以+1
            # 大于说明在下坡
            if nums[mid] > nums[mid+1]: right = mid
            else: left = mid + 1
        return right