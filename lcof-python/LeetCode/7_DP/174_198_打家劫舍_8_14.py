from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [nums[0]]
        dp.append(max(dp[0], nums[1]))
        for i in range(2, n):
            dp.append(max(dp[i-1], nums[i]+dp[i-2]))
        return dp[-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        # 记录第一个为0 而且不用开辟 o(n)空间
        for i in nums:
            prev, curr = curr, max(curr, prev + i)

        return curr