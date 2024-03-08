class Solution:
    def MoreThanHalfNum_Solution(self , numbers: List[int]) -> int:
        if not numbers:
            return -1
        n = len(numbers)
        temp = numbers[0]
        count = 1
		# 大于一半的本来就最多 其他的还自相残杀 最后多的一定是大于一半的
        for i in range(1,n):
            if count == 0:
                temp = numbers[i]
                count = 1
			# 相同的就加1 不同的就减一
            if numbers[i] == temp:
                count += 1
            if numbers[i] != temp:
                count -= 1
        return temp