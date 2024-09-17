class Solution:
    def FindNumbersWithSum(self , array: List[int], sum: int) -> List[int]:
        if not array:
            return []
        m,n =0, len(array)-1
        my_sum = array[m] + array[n]
        for i in range(1,len(array)):
            # 数组本身升序 直接左右开始滑动
            if my_sum > sum:
                my_sum -= array[n]
                n -= 1
                my_sum += array[n]
                continue
            elif my_sum < sum:
                my_sum -= array[m]
                m += 1
                my_sum += array[m]
                continue
            else:
                return [array[m], array[n]]
        return []