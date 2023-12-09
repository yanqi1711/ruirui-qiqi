class Solution:
    def findNthDigit(self , n: int) -> int:
        # write code here
        start = 1
        sum = 9
        digit = 1
        # 找到所在区间
        while n>sum:
            n -= sum
            digit += 1
            start *= 10
            # 必须是9 9 9*2*10 = 180 9*3*100=2700
            sum = 9 * digit * start
        # 找到的数字 10也是占2位 除以位数
        num = start + (n-1) // digit
        # 索引
        index = (n-1) % digit
        return  int(str(num)[index])