class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        val2index = {}
        for i in range(len(nums)):
            # nums[i] == nums[j]两个数要相等 
            if nums[i] in val2index and abs(i - val2index[nums[i]]) <= k:
                return True
            # 随时更新所有值 因为索引是越来越大的
            val2index[nums[i]] = i
        return False
