from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0,len(nums) -1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
        return nums[left]