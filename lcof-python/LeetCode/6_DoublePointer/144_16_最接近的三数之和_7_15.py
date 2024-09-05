class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return []
        # 排序
        nums.sort()
        closetSum = float('inf')
        length = len(nums)
        for i in range(length-2):
            x = nums[i]
            if i and x == nums[i-1]:
                continue
            # 双指针
            left,right = i+1 ,length-1
            #  一共要三个数 当然不能相等
            while left < right:
                cur = x + nums[left] + nums[right]
                if target > cur:
                    left += 1
                elif target < cur:
                    right -= 1
                else:
                    return target
                if abs(cur - target) < abs(closetSum - target):
                    closetSum = cur
        return closetSum