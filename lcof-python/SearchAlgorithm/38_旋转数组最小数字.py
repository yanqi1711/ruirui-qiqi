class Solution:
    def minNumberInRotateArray(self , nums: List[int]) -> int:
        # write code here
        if not nums:
            return 0
        # 二分查找
        left , right = 0, len(nums)-1
        # 相等就找到了
        while left < right:
            mid = (left + right) // 2
            #  大 大 大 小(mid) 小 小 小
            if nums[mid] < nums[right]:
                right = mid
            # 大 大 大 大(mid) 小 小 小
            elif nums[mid] > nums[right]:
                # 因为mid比right大了 并且其左边的数 一定大于等于right 所以最小值一定在右边 
                left = mid + 1
            #  2 2 2 2(mid) 1 1 2
            else:
                # 相等 所以需要最右边向前面试出最小值
                right -= 1
        return nums[left]