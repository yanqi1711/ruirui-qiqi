class Solution:
    def __init__(self) -> None:
        self.count = 0
        self.mod = 1000000007
    def merge(self, nums:List[int], left, mid, right):
        # 左右端点
        i = left
        j = mid + 1
        arr_n = []
        while i <= mid and j <= right:
            if nums[i] > nums[j]:
                arr_n.append(nums[j])
                j+=1
                # 重点 不是+1 因为第一个数组的数字比后面的第一个数字大
                # 则第一个数组数组后面的数字也比第一个大
                # [3] 6 9    [1] [4] [10]
                # 第一次要加3 第二次加2
                self.count += mid - i + 1
                self.count %= self.mod 
            else:
                arr_n.append(nums[i])
                i+=1
        while i <= mid:
            arr_n.append(nums[i])
            i+=1     
        while j <= right:
            arr_n.append(nums[j])
            j+=1
        nums[left:right+1] = arr_n
            
    def merge_sort(self, nums, left, right):
        # 1 分开
        # 2 合并时候从哪里开始
        # 不能一直划分
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(nums, left, mid)
            self.merge_sort(nums, mid+1, right)
            self.merge(nums, left, mid, right)

    def InversePairs(self , nums: List[int]) -> int:
        # 为什么此题的最优解法可以借助归并排序的思想？
        # 每一个逆序对其实就是排序时的交换(冒泡 归并)
        if not nums or len(nums) == 1:
            return self.count
        n = len(nums)
        left = 0
        right = n-1
        self.merge_sort(nums, left, right)
        print(nums)
        return self.count
