#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param k int整型 
# @return int整型
#
class Solution:
    count = 0
    def GetNumberOfK(self , nums: List[int], k: int) -> int:
        # write code here
        mid = len(nums) // 2
        if len(nums) == 0:
            return self.count
        # 等于k 去除k 再加
        # 归并排序->分治
        elif nums[mid] == k:
            self.count += 1
            return self.GetNumberOfK(nums[:mid]+nums[mid+1:],k)
        elif nums[mid] < k:
            return self.GetNumberOfK(nums[mid+1:], k)
        elif nums[mid] > k:
            return self.GetNumberOfK(nums[:mid], k)


    # 法二 调用 self.bisearch(data, k + 0.5) - self.bisearch(data, k - 0.5)
    def binsearch(self, data, k):
        left, right = 0, len(data) - 1
        # 第一种写法 left <= right 判定等于
        while left <= right:
            mid = (left + right) // 2
            # 重新划分边界 从mid开始
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right =  mid - 1
        return left