class Solution:
    def FindGreatestSumOfSubArray(self , array: List[int]) -> List[int]:
        # 需要记录最长空间
        if not array:
            return []
        left = 0
        right = 0
        max_left = 0
        max_right = 0
        max = 0
        result = array[0]
        for i in range(len(array)):
            max += array[i]
            right = i + 1
            # 只需要记录最大的index就可以 等于时计算为0的情况 因为需要数组长度最大
            if max >= result:
                result = max
                max_left = left
                max_right = right
            if max < 0:
                max = 0
                left = i + 1
        return array[max_left:max_right]