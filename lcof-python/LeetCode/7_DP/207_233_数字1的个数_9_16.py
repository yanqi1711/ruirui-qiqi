class Solution:
    # 规律 当前位数为0
    # 1的个数为 digit*high 
    # exampe: 2304 十位数上的数字为:0 则十位数上面1的个数位 23*10=230 
    # 因为0不包含1 所以对于题目而言  1x 就有10个1 但是一共有多少个1x呢 是 23个1x所以十位数字是230个1
    # 为1的时候 需要加上自己本身的情况 比如10 11 12 13 14需要加上自身的1 个数刚好等于 low(4)+10(1)=5
    # digit*high + low+1
    # others: digit*(high+1)   [2,3,4,5..9]因为已经把1全部包含了所以就直接进位
    def countDigitOne(self, n: int) -> int:
        digit,res=1,0
        high,cur,low= n//10, n%10,0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res