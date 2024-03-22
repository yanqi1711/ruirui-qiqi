class Solution:
    def reOrderArrayTwo(self , array: List[int]) -> List[int]:
        if not array:
            return []
        left,right = 0,len(array) - 1
        # 双指针
        while(left < right):
            # 为奇数 left后移
            if array[left] % 2 == 1:
                left += 1
            # 偶数判断right
            else:
                # 交换同时移动
                if array[right] % 2 == 1:
                    array[left] , array[right] = array[right], array[left]
                    left += 1
                    right -= 1
                # 没有交换 移动right
                else:
                    right -= 1
        return array