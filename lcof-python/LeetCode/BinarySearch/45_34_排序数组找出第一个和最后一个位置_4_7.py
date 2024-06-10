class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1  # 闭区间 [left, right]
            while left <= right:  # 区间不为空
                # 循环不变量：
                # nums[left-1] < target
                # nums[right+1] >= target
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1  # 范围缩小到 [mid+1, right]
                else:
                    right = mid - 1  # 范围缩小到 [left, mid-1]
            return left  # 或者 right+1
        left = lower_bound(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        # 如果 start 存在，那么 end 必定存在
        right = lower_bound(nums[left:],target+1) + left -1
        return [left, right]
        