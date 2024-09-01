from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        left,right = 0, len(numbers)-1
            
        # 双指针 2个数当然不能等于
        while left < right:
            x = numbers[left] + numbers[right]
            if x == target:
                return [left+1, right+1]
            elif x < target:
                left += 1 
            else:
                right -= 1
        return None