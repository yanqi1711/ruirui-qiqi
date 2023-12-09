class Solution:
    def __init__(self) -> None:
        self.nums = []
        # self.mid_nums = []
        self.mid = 0

    # 大顶堆
    def adjust_max_heap(self, pos, length):
        dad = pos
        son = pos * 2 + 1
        while son < length:
            if son + 1 < length and self.nums[son+1] > self.nums[son]:
                son += 1
            if self.nums[dad] < self.nums[son]:
                self.nums[dad], self.nums[son] = self.nums[son], self.nums[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def Insert(self, num):
        # write code here
        self.nums.append(num)
        n = len(self.nums)
        if n == 1:
            # self.mid_nums.append(num)
            return
        self.mid = n // 2
        for i in range(n // 2 -1,-1,-1):
            self.adjust_max_heap(i, n)
        # 全堆排超时 只需要排一半就行
        # -2 -3都行 -1 不行 左闭右开 
        for j in range(n-1,self.mid - 2,-1):
            self.nums[0], self.nums[j] = self.nums[j], self.nums[0]
            self.adjust_max_heap(0, j)
    def GetMedian(self):
        # write code here
        n = len(self.nums)
        if n == 1:
            return self.nums[0]
        if n % 2 == 0:
            return (self.nums[self.mid] + self.nums[self.mid - 1]) / 2
        else:
            return self.nums[self.mid]