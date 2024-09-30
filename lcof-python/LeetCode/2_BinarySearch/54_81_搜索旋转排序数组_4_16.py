class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        if n == 1:
            return nums[0] == target
        left, right = 0, n-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return True
            if nums[left] == nums[right]:
                left += 1
                continue
            # 2种情况
            if nums[mid] <= nums[right]:
                # target大于 所以 9 +E 1 1 6 7 8 target = 6
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    #  6 +E 1 6 7 8 9 target = 1
                    right = mid - 1
            else: # mid > right
                # 1 1 -999 100 1 1 1
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1 
                else:
                    left = mid+ 1
        return False
                