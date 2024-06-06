from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(x):
            # 目前总数为0 分组为1 (至少为1)
            total, cnt= 0, 1
            for i in nums:
                if total+ i > x:
                    cnt += 1
                    total = i
                else:
                    total += i
            # 小于 代表分大了 等于代表还能找到更小
            return cnt <= k
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
