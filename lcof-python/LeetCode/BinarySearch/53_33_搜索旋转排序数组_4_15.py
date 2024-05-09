class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums)
        if m == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        left,right = 0, len(nums) -1
        while left < right:
            mid = (left+right) >> 1
            if target < nums[mid]:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    if target > nums[right]:
                        right = mid
                    elif target < nums[right]:
                        left = mid + 1
                    else:
                        return right
            elif target > nums[mid]:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    if target < nums[right]:
                        left = mid + 1
                    elif target > nums[right]:
                        right = mid
                    else:
                        return right
            else:
                return mid
        return -1                    