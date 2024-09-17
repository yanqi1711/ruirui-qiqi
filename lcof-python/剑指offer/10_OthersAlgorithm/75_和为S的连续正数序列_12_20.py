class Solution:
    def FindContinuousSequence(self , sum: int) -> List[List[int]]:
        if not sum:
            return []
        i,j = 1,1
        res = []
        my_sum = 1
        # 至少包括两个数
        while i <= (sum // 2):
            if my_sum < sum:
                j += 1
                my_sum += j
                continue
            elif my_sum > sum:
                my_sum -= i
                i += 1
                continue
            else:
                temp = [ m for m in range(i,j+1)]
            my_sum -= i
            i+=1
            j+=1
            my_sum += j
            res.append(temp)
            temp = []
        return res