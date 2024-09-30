class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序 二重循环 剪枝 双指针
        nums.sort()
        ans = []
        n = len(nums)
        # 第一个数 后面到倒数第三个数就结束了
        for i in range(n-3):
            x = nums[i]
            # 去重 必须和之前的相比 因为之前的已经找到了 并且因为要去重 所以直接Continue 
            # 直接 i 就行 本质就代表 i>0
            if i and x == nums[i-1]:
                continue
            # 第一个数就比target大
            if x + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 最后三个数相加都比target小 直接下一个
            if x + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            # 找第二个数
            for j in range(i+1, n-2):
                y = nums[j]
                # 确保已经是第二个数
                if j > i+1 and y == nums[j-1]:
                    continue
                if x+y+nums[j+1]+nums[j+2] >target:
                    break
                if x+y+nums[-1]+nums[-2] < target:
                    continue
                # 双指针
                left = j+1
                right = n-1
                while left < right:
                    s = x + y + nums[left] + nums[right]
                    if s > target:
                        right-=1
                    elif s < target:
                        left+=1
                    else: # s == target 相等了
                        ans.append([x, y, nums[left], nums[right]])
                        # left向前
                        left+=1
                        # 如果当前left的值和之前的相等 就去重
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        # 因为前面的left的值一定和之前的不一样(不然就跳出循环了)所以right也要移动并去重
                        right-=1
                        while right > left and nums[right] == nums[right+1]:
                            right-=1
        return ans