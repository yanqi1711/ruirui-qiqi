class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 把环拆开 
        pre,cur1 = 0,0
        for i in nums[:-1]:
            pre,cur1 = cur1, max(pre+i, cur1)
        pre, cur2 = 0,0
        for i in nums[1:]:
            pre,cur2 = cur2, max(pre+i, cur2)
        return max(cur1, cur2)