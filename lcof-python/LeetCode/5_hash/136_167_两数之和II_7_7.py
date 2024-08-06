from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        left,right = 0, len(numbers)-1
            # 二分查找
        while left < right:
            x = numbers[left] + numbers[right]
            if x == target:
                return [left+1, right+1]
            elif x < target:
                left += 1 
            else:
                right -= 1
        return None
# 可以用在3数之和
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        for i in range(len(numbers)-1):
            # 双指针 用while 因为索引需要每次变化 而for是固定的
            left,right = i+1, len(numbers)-1
            x = target - numbers[i]
            # 二分查找
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == x:
                    return [i+1 , mid+1]
                elif numbers[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
        return None