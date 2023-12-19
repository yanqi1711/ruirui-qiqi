class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # bit 代表位数 个位 十位 百位 
        # high代表高位 low代表当前位数的更低位
        # 502223 bit = 100 high = 502 low = 23
        # cur = num/bit%10
        # cur > 1 : (high + 1) * bit
        # cur = 1 : high * bit + (1+low) 自身1 + 23个1即：100~123
        # cur = 0 ：high * bit 0~4 = 5
        bit = 1
        sum = 0
        while(bit <= n):
            cur = (n // bit) % 10
            # 213 % 1 = 0
            low = n % bit
            high = n // bit // 10
            if cur > 1:
                sum += (high + 1) * bit
            elif cur == 1:
                sum += high * bit + (1+low)
            else:
                sum += high * bit
            bit = bit * 10
        return sum