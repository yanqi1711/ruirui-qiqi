class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 当前能到达的最远位置
        curMax = 0
        # 右边界
        end = 0
        # 结果
        ans = 0
        for i in range(len(nums)-1):
            # 捕获最大可达地点
            curMax = max(curMax, i+nums[i])
            # 到了当前能到的最大边界 说明 这次跳跃格子到达极限了,再跳一次找新边界 新边界就是上面存储的
            # 本质上是找每次jump到达的最远距离, 贪心
            if i == end:
                end = curMax
                ans += 1
        return ans
