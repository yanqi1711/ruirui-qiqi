from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return -1
        left, right = 0, len(height) - 1
        curMax = 0
        while left < right:
            curArea = min(height[left], height[right]) * (right - left)
            if curArea > curMax:
                curMax = curArea
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return curMax
# 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        maxh = max(height)
        while left < right and max_area <= maxh * (right - left):
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area