class Solution:
    # 小顶堆 
    # 小堆就是把小的放在后面 [..., 4,3,2,1]
    # 所以需要反切片
    def adjust_min_heap(self, nums, pos, length):
        dad = pos
        son = dad * 2 + 1
        while son < length:
            if son + 1 < length and nums[son] > nums[son+1]:
                son += 1
            if nums[dad] > nums[son]:
                nums[dad], nums[son] = nums[son], nums[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self, nums,k):
        n = len(nums)
        for i in range(n // 2 -1, -1,-1):
            self.adjust_min_heap(nums, i, n)
        for j in range(n-1, n-k- 1,-1):
            nums[0], nums[j] = nums[j], nums[0]
            self.adjust_min_heap(nums, 0, j)
        
    def GetLeastNumbers_Solution(self , input, k: int) -> [int]:
        self.heap(input,k)
        return input[-1:-k-1:-1]

        # 直接调库
        # import heapq
        # return heapq.nsmallest(k,input)