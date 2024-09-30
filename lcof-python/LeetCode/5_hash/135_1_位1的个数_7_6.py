class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n>0:
            print(n)
            if n & 1 == 1:
                cnt+=1
            n >>= 1
        return cnt
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n>0:
            # n & (n−1) 运算结果恰为把 n 的二进制位中的最低位的 1 变为 0 之后的结果 
            # 可以加速为含有1的个数
            n &= n - 1
            cnt+=1
        return cnt