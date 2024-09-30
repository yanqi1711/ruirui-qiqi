class Solution:
    # 滑动窗口 需要for+while循环
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        cnt = float('inf')  # 使用正无穷大初始化最小长度
        sumValue = 0  # 当前窗口的和
        l = 0  # 左指针
        # while的话 需要在外面进行一次min操作 但是这样很难判断 最后一个数极爱起来是否>=target
        for i in range(len(nums)):
            sumValue += nums[i]
            # 在循环里面算cnt可以不用在外面+2
            # 不需要先判断
            while sumValue>=target:
                cnt = min(cnt, i - l + 1)  # 更新最小长度
                sumValue -= nums[l]  # 移动左指针
                l += 1  # 左指针右移
        return 0 if cnt == float('inf') else cnt