class Solution:
    # 
    def adjust_heap(self, nums, pos, length):
        dad = pos
        son = 2 * pos + 1
        while son < length:
            # 先比较儿子
            if son + 1 < length and str(nums[son]) + str(nums[son+1]) < str(nums[son + 1]) + str(nums[son]):
                son += 1
            # 比较父亲和最小的儿子
            if str(nums[dad]) + str(nums[son]) < str(nums[son]) + str(nums[dad]):
                nums[dad], nums[son] = nums[son], nums[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break
    def heap(self, nums):
        n = len(nums)
        # 从堆中间开始构建大顶堆
        for i in range(n//2-1,-1,-1):
            self.adjust_heap(nums,i,n)
        # 交换 然后继续调整堆
        for j in range(n-1,-1,-1):
            nums[0], nums[j] = nums[j], nums[0]
            self.adjust_heap(nums, 0, j)
    def PrintMinNumber(self , numbers) -> str:
        if not numbers:
            return ''
        self.heap(numbers)
        numbers = list(map(str, numbers))
        print(numbers)
        return ''.join(numbers)