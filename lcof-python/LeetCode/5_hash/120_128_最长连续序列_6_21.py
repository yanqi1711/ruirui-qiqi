from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        nums = set(nums)

        # 
        for i in nums:
            # 不在说明是起点 不是起点就下一个数
            if i-1 not in nums:
                cur = i
                cur_count = 1
                while cur + 1 in nums:
                    cur +=1
                    cur_count +=1
                
                # 寻找完毕 找最大值
                count = max(count, cur_count)
        return count
