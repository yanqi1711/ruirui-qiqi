class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        first, end = 0,len(nums)
        while first < end:
            # while循环 需要注意可能超过 first < end的界限
            while nums[end-1] == val:
                end -= 1
                if first == end:
                    return end 
            while nums[first] != val:
                first += 1
                if first == end:
                    return end 
            if first < end:
                nums[first],nums[end-1] = nums[end-1], nums[first]
            print(nums)
        return end