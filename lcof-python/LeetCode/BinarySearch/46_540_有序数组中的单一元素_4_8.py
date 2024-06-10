from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0,len(nums) - 1
        # 相等时就找到了
        while left < right:
            mid = (left + right) >> 1
            # 在未出现单一元素时 
            # 偶数索引向后+1 奇数向后-1 
            if nums[mid] == nums[mid^1]:
                left = mid + 1
            # 跳过单一元素后
            else:
                right =  mid
        return nums[left]

        # res = 0
        # for i in nums:
        #     res = res ^ i
        # return res