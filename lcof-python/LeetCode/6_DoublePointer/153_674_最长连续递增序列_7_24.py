class Solution:
    # 遍历
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = 1
        count = 1
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans