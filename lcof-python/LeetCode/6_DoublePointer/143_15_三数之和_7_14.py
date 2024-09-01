class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ans = []
        # 排序
        nums.sort()
        if nums[-1] < 0 or nums[0] > 0:
            return ans
        length = len(nums)
        for i in range(length-2):
            x = nums[i]
            if i and x == nums[i-1]:
                continue
            # 前面数大于0 说明不可能更小了 直接出去 如果小于0说明符合情况要去 剩下的数组用 双指针找
            if x + nums[i+1] + nums[i+2] > 0:
                break
            # 加上后面最大两个数 还是小于0 直接下一个
            if x + nums[-1] + nums[-2] < 0:
                continue
            # 双指针
            left,right = i+1 ,length-1
            #  一共要三个数 当然不能相等
            while left < right:
                target = x + nums[left] + nums[right]
                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    ans.append([x, nums[left], nums[right]])
                    # 超级重点 需要去重 因为可能存在不止一个解
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans