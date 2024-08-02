class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 面对流数据需要用二分搜索 两个单调栈
        # 根据题意一般情况 j 一般是某个list切片离最大的值
        # 在左边找最小的 右边找最大的 适用于一般情况
        # 9  1 6 3 -> 1 6 3
        stack = []
        k = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            # 如果是第一次 k是最小的 不可能触发
            # 之后k 如果是list的最大值 也不会跳入
            # 这一行就是找 已经遍历过区间的i 和 k的值 
            # 已经出现过k说明已经找到了区间最大值 
            # 现在i只需要比k小直接返回True
            if nums[i] < k:
                return True 
            # 开始找k 单调(增)栈维护
            # 1 4 [1 2 3] 查找满足j > k的最大值  也就是右边的最大值
            while stack and stack[-1] < nums[i]:
                # 每次把栈顶的值pop出现 找单调栈内满足情况的最大值
                k = max(k, stack.pop())
            # 因为上面每次都会找到最大值所以 这里可以随便
            stack.append(nums[i])
        return False