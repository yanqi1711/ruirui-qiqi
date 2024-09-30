class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def getBucketIdx(u):
            return u // size
        # 确保分配到相差 valueDiff个区间 因为abs(nums[i] - nums[j]) <= valueDiff
        #  valueDiff = 3 size = 4 (0,1,2,3, | 4,5,6,7)
        size = valueDiff + 1
        # {桶id:对应的值} 本质上维护在indexDiff+1个桶
        map = {}
        for i,val in enumerate(nums):
            idx = getBucketIdx(val)
            # # 目标桶已存在（桶不为空），说明前面已有 [u - t, u + t] 范围的数字
            if idx in map:
                return True
            # 检查邻近的桶 例:idx=1 val=4 map={0:3} 
            if idx-1 in map and abs(val - map[idx-1]) <= valueDiff:
                return True
            # 同理
            if idx+1 in map and abs(val-map[idx+1]) <= valueDiff:
                return True
            # 更新桶 因为map本质上是维护indexDiff+1个桶 所以每次都要update
            map[idx] = val
            if i >= indexDiff:
                # 因为i马上会自加1所以需要删去最开始那个元素的桶 
                # 因为有符合条件的桶只有一个元素 因为出现两个的话直接返回True了
                map.pop(getBucketIdx(nums[i-indexDiff]))
        return False